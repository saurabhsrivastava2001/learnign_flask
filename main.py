from website import create_app
app = create_app()
if __name__=='__main__': #only if we run the code not import
    app.run(debug=True)  #its gonna run the app every time we make the changes to the code 
    