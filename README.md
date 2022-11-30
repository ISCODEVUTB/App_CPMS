# App_CPMS
CleanShop es un E-commerce orientado en microservicios, a continuación, se explicarán estos servicios junto con su respectiva URI almacenado en Render, estos servicios son: 

###### Stock (Django): Servicio donde almacena todos los artículos de limpieza de la base de datos, almacenado en postgree sql y a la vez esta está desplegada en render.

###### URI del servicio: https://stock-serviceutb.onrender.com
 
###### Métodos: 

###### GET:
-	/products
-	/products/active
-	/products/popular
-	/products/:id
-	/products/active/:id
-	/products/type?type=Industrial
-	/products/search?name=trapero

###### POST:
-	/products/ Se debe suministrar un body con la información del producto:

{
   "Name": "",
   "Desc": "",
  "Type": "" (H, L, I),
  "Quantity": int,
  "Price": int
  "Product_pic": null,
  "Active": false by default,                                 
  "Provider_id": "No provider" by default or null,
  "Provider_id_prod": 0 by default or null
}
- /products/addFromProvider?name=BestCleanning&id_prod=1&quantity=20 Se suministra en los parámetro de la URI el nombre de proveedor el id el producto que se quiere añadir y la cantidad del producto que se quiere añadir.

###### PUT:
- /products/ Se debe suministrar un body con la información a actualizar:
{
   "id": 6,
   "Name": "Axión",
   "Desc": "wouhiebiwkroinonr",
   "Type": "L",
   "Quantity": 50,
   "Price": 20000,
   "Provider_id": "No provider",
   "Active": true,
   "Provider_id_prod": 0
}

###### DELETE:
- /products/:id 

###### Carrito (FastAPI): Servicio donde se le concede al usuario registrado, el privilegio de 
almacenar sus productos escogidos y así pagarlos todos en una sola compra.

###### URI del servicio: https://cart-serviceutb.onrender.com/docs/


###### Lista de deseos (FastAPI): servicio donde se le otorga al usuario registrado, el beneficio 
de almacenar sus productos en una lista. Solo que, en este servicio, a diferencia del carrito de compras. El usuario no puede hacer sus compras en una sola orden. Solo es un servicio donde se guarda las preferencias del usuario y así que este las compre cuando deseen.

###### URI del servicio: https://wishlist-serviceutb.onrender.com/docs/


###### Servicio de Proveedores (FastAPI): este servicio es el que permite la comunicación entre proveedores y CleanShop. Cuando falte alguna cantidad de productos en el E-commerce esta será la comunicación directa entre el administrador y los proveedores.

###### URI del servicio: https://provider-serviceutb.onrender.com/docs


###### Servicio de Autenticación (Django): Este servicio permite la autenticación de los usuarios y al arrojar dos tokens para verificar la identidad del usuario al momento de hacer login. Y es esencial al momento de utilizar la mayoría de los servicios (carrito y lista de deseos), ya que sin él, no se podrían utilizar.

###### URI del servicio: https://auth-servicetub.onrender.com

###### Métodos: 

###### GET:
-	/user/:id

###### POST:
-	/login
-	
- /user/create Se suministra en los parámetro de la URI el nombre de proveedor el id el producto que se quiere añadir y la cantidad del producto que se quiere añadir.

###### PUT:
- /user/modify/:id Se suministra el body de la actualización. 


