# from tkinter import messagebox
# import folium, webbrowser, os
#
# #creating map object and displaying city location in web browser based on latitude and longitude recived via API
# def showOnMap(longitudeLabel, latitudeLabel):
#     longitude = longitudeLabel['text'].split(" ")[1]
#     latitude = latitudeLabel['text'].split(" ")[1]
#     if longitude != "":
#         new = 2
#         map = folium.Map(location=[latitude, longitude], zoom_start=13)
#         marker_text = '''<font face='Bahnschrift'>Weather forecast location</font>'''
#         iframe = folium.IFrame(marker_text, width=220, height=35)
#         popup = folium.Popup(iframe, min_width=220, max_width=220)
#         folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon("blue")).add_to(map)
#         map.save('map.html')
#         map_html = 'map.html'
#         webbrowser.get('windows-default').open('file://' + os.path.realpath(map_html))
#     else:
#         messagebox.showwarning('Error', "Search for a city first!")
