import mysql.connector

def update_product_prices():
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',          
        user='root',      
        password='your_password',  
        database='database1'   
    )
    
    try:
        cursor = connection.cursor()
        
        # Update prices by increasing them by 10%
        update_query = "UPDATE products SET price = price * 1.10"
        cursor.execute(update_query)
        connection.commit()  # Commit the changes
        
        # Select the updated product names and their new prices
        select_query = "SELECT name, price AS new_price FROM products"
        cursor.execute(select_query)
        
        # Fetch all the results
        results = cursor.fetchall()
        
        # Display the results
        for row in results:
            print(f"Product Name: {row[0]}, New Price: {row[1]:.2f}")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Call the function to update prices and display results
update_product_prices()