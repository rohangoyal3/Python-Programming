from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle         #reportlab used for generation of pdf
from reportlab.lib import colors                                                       #platypus used for page layout  and colours
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

# data to be displayed in table
DATA = [ 
	[ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
	[ 
		"21/11/2020", 
		"Full Stack Development with React & Node JS - Live", 
		"Lifetime", 
		"11,999.00/-", 
	], 
	[ "22/11/2020", "Learning Python: Live Session", "6 months", "12,999.00/-"], 
	[ "Sub Total", "", "", "24,9998.00/-"], 
	[ "Discount", "", "", "-3,000.00/-"], 
	[ "Total", "", "", "21,998.00/-"], 
] 
 
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 )             # creating a document template
 
styles = getSampleStyleSheet() 										# standard stylesheet defined within reportlab itself

title_style = styles[ "Heading1" ] 									# fetching the style heading (Heading1) 

title_style.alignment = 1											# 0: left, 1: center, 2: right (Text alignment)
 
title = Paragraph( "Payment Receipt" , title_style ) 				# creating the paragraph with the heading text and passing the styles of it

# creates a Table Style object and in it, 
# defines the styles row wise 
# the tuples which look like coordinates 
# are nothing but rows and columns 
style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
		( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
	] 
) 

# creates a table object and passes the style to it 
table = Table( DATA , style = style ) 

pdf.build([ title , table ]) 										# final step which builds the actual pdf putting together all the elements 