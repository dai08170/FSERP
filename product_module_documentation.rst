#partial doccumentation file
Definintions:
The product module consists of defition for various parameters and references that a product may have.

It defines a variety of things such as Category of Unit of Measure(UOM), Unit of Measure, Product Category, Product Template and Product, Configuration.

We will explain the above definitions with respect to the code in trytond/modules/product/product.py

Basic:
The basic Product module begins with __init__.py where it uses trytond.pool.Pool to register several important class like Uom from uom.py etc.

It is mandatory to register a module in Pool as trytond imports a Module from pool and not from the directory.

Implementation:

1)product.py

	This file has two important classes Template and Product these are equivalent to the Product Template and Product defined in the definitions section.

	These classes are defined in active record pattern.

	class 1: Template

	The Product Template has a class Template that extends ModelSQL and ModelView

	These base class provides the basic implementation for creating a database entry and also providing the data to the client sidethrough views.


	This class defines 
	1.Name: Name of the product
	2.Type: Goods,Assets,Service
	3.Category:many2one relation to the produt.category module i.e Category class from the category.py file in the same directory
	4.List Price: the default Sale Price
	5.List Price UOM: the unit of list price
	6.Cost Price: The cost of one unit
	7.Cost Price UOM: The usnit of cost price
	8.Cost Price Method: 'Fixed' or 'Average', Defines how the cost price should be updated.
Fixed- means unchanged
Average- Average means average of items that are in the stock
	9. Default UOM: used to express the Stock levels
	10.Active : Allow to disable a product

	11. Important Method:
		1.create(vlist):
			""" :param: vlist is the local variable list of the class that needs to be passed as they carry the value to be saved in the db"""
			Saves the vlist attributes to the db

	class 2: Product

	This class extends the basic Template class with some additional fields like code and description of the product

	An important feature of the Product class is that its template variable requires a Template class instance before being saved into the db.
2)uom.py
	This file has two important classes UomCategory and Uom which are the corresponding classes of Category of Unit of Measure and Unit of Measure

	class 1:Category of Unit of Measure or UomCategory:

		This class extends ModelSQL and ModelView

		These base class provides the basic implementation for creating a database entry and also providing the data to the client sidethrough views.

		It is simply defined by attribute name

	class 2:Unit of Measure or Uom:
			This class defines the units used to measure for the product.
			It defines the following attibutes
			1.name:Name of the unit
			2.symbol:Symbol of the unit used
			3.uomCategory:It is used to define the category of the uom i.e an instance of UomCategory used for grouping
			4.rate and factor: It is the unit rate and factor is the inverse of the rate.
			5.rounding precision: It is used for rounding the floating numbers.
			6.digits: It is the number of digits till which the value is represented
			7.active: allows to disable a uom

3)category.py
	This file has a class Category which is equivalent to the Product Category defined in the definitions section.
	class 1:Category:
		composed of a name
		It helps to categorize a product.
		The product categories are organized in a tree structure.

4)configuration
	This uses section 'product' to retrive some parameters
	'price_decimal' defines the number of decimal with which the unit prices are stored. The default value is '4'
	Warning: It cannot be lowered once database is created
	This configuration is done in the product.py price_digits global variable which uses config from trytond.config which creates a int of digits to be used in Template and Product class.
