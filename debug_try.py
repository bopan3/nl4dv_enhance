import sys  
# sys.path.append("/Users/panbo/Desktop/nl4dv_enhance")
# sys.path.append("../../../../")
# sys.path.append("../../../")
# sys.path.append("../../")
# sys.path.append("../")

from nl4dv import NL4DV

# nl4dv_instance = NL4DV(debug=False,verbose=False,alias_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/aliases/movies-w-year.json",data_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/data/movies-w-year.csv")
nl4dv_instance = NL4DV(debug=False,verbose=False,alias_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/aliases/olympic_medals.json",data_url="/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/data/olympic_medals.csv")
dependency_parser_config = {'name': 'corenlp','model': "/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/jars/stanford-english-corenlp-2018-10-05-models.jar",'parser': "/Users/panbo/Library/Mobile Documents/com~apple~CloudDocs/Documents/VIS/nl4dv_modify/examples/assets/jars/stanford-parser.jar"}
nl4dv_instance.set_dependency_parser(config=dependency_parser_config)

# nl4dv_instance.analyze_query("Show the relationship between budget and rating for Action and movies that grossed over 100M")
# nl4dv_instance.render_vis("Show average gross across genres for science fiction")
# nl4dv_instance.render_vis("fantasy movies")
# nl4dv_instance.render_vis("science fiction")
# nl4dv_instance.render_vis("create a barchart showing average gross across genres")
# nl4dv_instance.render_vis("Show average gross across genres for science fiction")
# nl4dv_instance.render_vis("gross over 100M")
nl4dv_instance.render_vis("show me medals for hockey and skating by country")





