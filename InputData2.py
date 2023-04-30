from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST'])
def order():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    product_name = request.form['product_name']
    quantity = request.form['quantity']
    order_description = request.form['order_description']
    payment_proof = request.files['payment_proof']
    
    # simpan data order ke file excel
    data = {'Nama': [name], 'Email': [email], 'No HP': [phone], 'Produk': [product_name], 'Jumlah': [quantity], 'Deskripsi Pesanan': [order_description]}
    df = pd.DataFrame(data)
    df.to_excel('order.xlsx', index=False)
    
    # simpan image pembayaran ke file khusus
    payment_proof.save('payment_proof.jpg')
    
    return 'Order berhasil!'

if __name__ == '__main__':
    app.run(debug=True)
