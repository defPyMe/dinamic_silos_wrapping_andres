from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import datetime

wn = str(datetime.datetime.today().isocalendar()[1])

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    #add logo 
      # Add an image
    image_path = "ferrero_logo.PNG"  # replace with your image path
    c.drawImage(image_path, 0.1 * inch, height - 1.17 * inch, width=1.3 * inch, height=1.3 * inch)

  #calculating current week number 
    

    # Add title
    c.setFont("Helvetica-Bold", 15)
    c.drawString(2.6 * inch, height - 0.8 * inch, f"Week {str(wn)} Update Mat. 72901844")

    # Add some text
    c.setFont("Helvetica", 10)
    text = "Weekly report generated automatically to monitor present and future Cocoa Butter"
    c.drawString(1.6 * inch, height - 1.2 * inch, text)

    #changing teh font as it is body now
    c.setFont("Helvetica", 12)
    #first description of the siloses stock 
    text = """Current situation of the silos in possession and forecasted total quantity they contain"""
    c.drawString(0.5 * inch, height - 1.6 * inch, text)
    #text = """13 isotanks as per best scenarios, the quantity melted can be adjusted accordingly to observation."""
    #c.drawString(0.5 * inch, height - 2.7 * inch, text)
    #text = """Previous week to the current contains the actual status of the silos, week 1 to 4 represent the """
    #c.drawString(0.5 * inch, height - 2.9 * inch, text)#going down line by line witha  change of.2
    #text = """weeks from current to current + 3 with projected statuses of the silos."""
    #c.drawString(0.5 * inch, height - 3.1 * inch, text)#going down line by line witha  change of.2
    # Add an image
    image_path = "first_4_weeks_silose.png"  # replace with your image path
    c.drawImage(image_path, 1 * inch, height - 4.2 * inch, width=6.5 * inch, height=2.5 * inch)
    #add additional text as second description

    #first description of the siloses stock 
    text = """Quantity in Genova in isotanks, quantity melted in silos and the total coverage in Weeks"""
    c.drawString(0.5 * inch, height - 4.6 * inch, text)
    #text = """port that will need to be processed in the followiing weeks. The last two columns represent the """
    #c.drawString(0.5 * inch, height - 6.7 * inch, text)
    #text = """occupancy in percentage (showing the total storage space using in the silos consideringa  total """
    #c.drawString(0.51 * inch, height - 6.9 * inch, text)#going down line by line witha  change of.2
    #text = """available of 1650 tons) and the coverage in weeks considering current/forecasted consumption."""
    #c.drawString(0.51 * inch, height - 7.1 * inch, text)#going down line by line witha  change of.2

    #putting up second table
    image_path = "styled_dataframe.png"  # replace with your image path
    c.drawImage(image_path, .7 * inch, height - 5.8 * inch, width=7 * inch, height=1 * inch)


    #c.showPage()  #add a new page, from now on c will add to the new page 
    #logo
   # image_path = "ferrero_logo.PNG"  # replace with your image path
    #c.drawImage(image_path, 0.1 * inch, height - 1.5 * inch, width=1.7 * inch, height=1.6 * inch)

    text = """Silos cycles and quantity of butter in Genova for the considered horizon"""
    c.drawString(0.5 * inch, height - 6.08 * inch, text)
   # text = """ up until week 35 of 2025) and the projected quantity of butter in tons that will remain in Genova."""
   # c.drawString(0.5 * inch, height - 2 * inch, text)
   # text = """The idea is to show if we will have any bottlenecks both in storage and utilization of silos space """
   # c.drawString(0.51 * inch, height - 2.2 * inch, text)#going down line by line witha  change of.2
    #text = """weeks from current to current + 3 with projected statuses of the silos."""
    #c.drawString(0.51 * inch, height - 2.4 * inch, text)#going down line by line witha  change of.2



    # Add an image
    image_path = "Andres_graph.png"  # replace with your image path
    c.drawImage(image_path, .5 * inch, height - 8.7 * inch, width=7.2 * inch, height=2.5 * inch)





    #change the style of the last title
    c.setFont("Helvetica", 10)



    #last description
    text = """Peaks in silos \"full\" status expressed in number of weeks                       Isotanks melted in previous weeks """
    c.drawString(0.8 * inch, height - 9 * inch, text)
    #text = """by the above graph. The idea is to highlight how close we will get to the 6 weeks limit imposed"""
    #c.drawString(0.5 * inch, height - 6.2 * inch, text)
    #text = """by quality when the butter has been melted. As it is a projection based on forecasted consumption """
    #c.drawString(0.51 * inch, height - 6.4 * inch, text)#going down line by line witha  change of.2
    #text = """it can be used to make adjustments and avoid \"expiration\" in the silos."""
    #c.drawString(0.51 * inch, height - 6.6 * inch, text)#going down line by line witha  change of.2

    #adding quality image table
    # Add an image
    image_path = "styled_quality.png"  # replace with your image path
    c.drawImage(image_path, 1.2 * inch, height - 10.25 * inch, width=3.5 * inch, height=1.2 * inch)

    image_path = "loaded.png"
    c.drawImage(image_path, 5.2 * inch, height - 10 * inch, width=2 * inch, height=1 * inch)
    

    c.setFont("Helvetica", 6)
    text = """* Unloading of silos has slowed down in recent weeks due to """
    c.drawString(5.3 * inch, height - 10.05 * inch, text)
    #capacity problems
    text = """capacity problem"""
    c.drawString(5.35 * inch, height - 10.15 * inch, text)


    #text = """2"""
    #c.drawString(7.8 * inch, height - 10.9 * inch, text)#going down line by line witha  change of.2
        #write the page number 
    #text = """1"""
    #c.drawString(8.09 * inch, height - 10.71 * inch, text)#going down line by line witha  change of.2
    #
    c.setFont("Helvetica", 10)
    text = """___________________________________________________________________________"""
    c.drawString(1.42 * inch, height - 10.5 * inch, text)#going down line by line witha  change of.2
    #
    # Save the PDF
    c.save()

create_pdf(f"Cocoa Butter report week {str(wn)}.pdf")
