import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="E:/Vendor Project/log/get_vendor_summary.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
def create_vendor_summary(conn):

    '''THis function will be merged the different tables to get the overall vendor summary and adding new columns in the resultant data'''

    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),
    PurchaseSummary AS (
        SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price as ActualPrice,
            pp.Volume,
            SUM(p.Quantity) as TotalPurchaseQuantity,
            SUM(p.Dollars)  as TotalPurchaseDollars
        FROM purchases p
                 JOIN purchase_prices pp
                      ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand,p.Description, p.PurchasePrice,pp.Price, pp.Volume
    ),
    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars)  AS TotalSalesDollars,
            SUM(SalesPrice)    AS TotalSalesPrice,
            SUM(ExciseTax)     AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )
    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
           AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
        """, conn)
    return vendor_sales_summary

def clean_data(vendor_sales_summary):
    '''This function will clean the data'''
    #Changing datatype to float
    vendor_sales_summary['Volume'] = vendor_sales_summary['Volume'].astype(float)

    # Filling the missing value
    vendor_sales_summary.fillna(0, inplace=True)

    #remving spaces from categorical columns
    vendor_sales_summary['VendorName'] = vendor_sales_summary['VendorName'].str.strip()
    vendor_sales_summary['Description'] = vendor_sales_summary['Description'].str.strip()

    #creating new columns for better analysis
    # Create a columns name is grossProfit (Sales - Purchase)
    vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars'] - vendor_sales_summary['TotalPurchaseDollars']
    # Create a column name is profit Margin ((grossProfit / Total sales) * 100)
    vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit'] / vendor_sales_summary['TotalSalesDollars']) * 100
    # Create a column name is Stock Turn Over (TotalSalesQuantity - TotalPurchaseQuantity)
    vendor_sales_summary['StockTurnOver'] = vendor_sales_summary['TotalSalesQuantity'] / vendor_sales_summary['TotalPurchaseQuantity']
    # Create a column name is Sales to Purchase ratio (TotalSalesDollar/TotalPurchaseDollar)
    vendor_sales_summary['SalesToPurchaseRatio'] = vendor_sales_summary['TotalSalesDollars'] / vendor_sales_summary['TotalPurchaseDollars']

    return vendor_sales_summary

if __name__ == "__main__":
    #creating database connection
    conn = sqlite3.connect("inventory.db")

    logging.info("Creating vendor summary table.....")
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info("Cleaning data.....")
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting data.....")
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info("Connected")
