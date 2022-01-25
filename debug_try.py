import sys  
# sys.path.append("/Users/panbo/Desktop/nl4dv_enhance")
# sys.path.append("../../../../")
# sys.path.append("../../../")
# sys.path.append("../../")
# sys.path.append("../")

from nl4dv import NL4DV
# data for movie
nl4dv_instance = NL4DV(debug=False,verbose=False,alias_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/aliases/movies-w-year.json",data_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/data/movies-w-year.csv")
# data for Olympics
# nl4dv_instance = NL4DV(debug=False,verbose=False,alias_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/aliases/olympic_medals.json",data_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/data/olympic_medals.csv")
dependency_parser_config = {'name': 'corenlp','model': "/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/jars/stanford-english-corenlp-2018-10-05-models.jar",'parser': "/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/jars/stanford-parser.jar"}
nl4dv_instance.set_dependency_parser(config=dependency_parser_config)

# nl4dv_instance.analyze_query("Show the relationship between budget and rating for Action and movies that grossed over 100M")
# nl4dv_instance.render_vis("Show average gross across genres for science fiction")
# nl4dv_instance.render_vis("fantasy movies")
# nl4dv_instance.render_vis("science fiction")
# nl4dv_instance.render_vis("create a barchart showing average gross across genres")
# nl4dv_instance.render_vis("Show average gross across genres for science fiction")
# nl4dv_instance.render_vis("gross over 100M")
# nl4dv_instance.render_vis("show me medals for hockey and skating by country")
# nl4dv_instance.render_vis("year is 2019")
# nl4dv_instance.render_vis("show average genre across different gross")
# nl4dv_instance.render_vis("show me the correlation of the budget and the ratings")
# nl4dv_instance.render_vis("show me the relationship between the budget and the ratings")
# nl4dv_instance.render_vis("gross over 200M")
# nl4dv_instance.render_vis("use a piechart to show genres")
# nl4dv_instance.render_vis("Relationship between IMDB Rating and Rotten Tomatoes Rating")
# nl4dv_instance.render_vis("show the budget and the rating as a bar chart")
# nl4dv_instance.render_vis("what is the worldwide gross distribution per genre")
nl4dv_instance.render_vis("gross across genres")











