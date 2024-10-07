from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')



@app.route("/submit")
def render_page_2():
    if "q1" in request.args:
        q1 = request.args["q1"]
    else:
        q1 = False
        
    if "q2" in request.args:
        q2 = request.args["q2"]
    else:
        q2 = False
        
    if "q3" in request.args:
        q3 = request.args["q3"]
    else:
        q3 = False
    
    if "q4" in request.args:
        q4 = request.args["q4"]
    else:
        q4 = False
        
    if "q5" in request.args:
        q5 = request.args["q5"]
    else:
        q5 = False
        
    if "q6" in request.args:
        q6 = request.args["q6"]
    else:
        q6 = False
    
    
    
    blockList = ["dirt","stone","log","iron ore","cobblestone","diamond ore","netherrack","glowstone"]
    
    if q1 == "brown":
        blockList.remove("stone")
        blockList.remove("iron ore")
        blockList.remove("cobblestone")
        blockList.remove("diamond ore")
        blockList.remove("netherrack")
        blockList.remove("glowstone")
    else:
        blockList.remove("dirt")
        blockList.remove("log")
        
    if q2 == "useful":
        if "dirt" in blockList:
            blockList.remove("dirt")
        if "netherrack" in blockList:
            blockList.remove("netherrack")
    else:
        if "stone" in blockList:
            blockList.remove("stone")
        if "iron ore" in blockList:
            blockList.remove("iron ore")
        if "cobblestone" in blockList:
            blockList.remove("cobblestone")
        if "diamond ore" in blockList:
            blockList.remove("diamond ore")
        if "log" in blockList:
            blockList.remove("log")
        if "glowstone" in blockList:
            blockList.remove("glowstone")
        
    if q3 == "overworld":
        if "glowstone" in blockList:
            blockList.remove("glowstone")
        if "netherrack" in blockList:
            blockList.remove("netherrack")
    else:
        if "stone" in blockList:
            blockList.remove("stone")
        if "dirt" in blockList:
            blockList.remove("dirt")
        if "iron ore" in blockList:
            blockList.remove("iron ore")
        if "cobblestone" in blockList:
            blockList.remove("cobblestone")
        if "diamond ore" in blockList:
            blockList.remove("diamond ore")
        if "log" in blockList:
            blockList.remove("log")
        
    if q4 == "ore":
        if "glowstone" in blockList:
            blockList.remove("glowstone")
        if "netherrack" in blockList:
            blockList.remove("netherrack")
        if "stone" in blockList:
            blockList.remove("stone")
        if "dirt" in blockList:
            blockList.remove("dirt")
        if "cobblestone" in blockList:
            blockList.remove("cobblestone")
        if "log" in blockList:
            blockList.remove("log")
    else:
        if "iron ore" in blockList:
            blockList.remove("iron ore")
        if "diamond ore" in blockList:
            blockList.remove("diamond ore")
    
    if q5 == "obtainable":
        if "stone" in blockList:
            blockList.remove("stone")
        if "iron ore" in blockList:
            blockList.remove("iron ore")
        if "diamond ore" in blockList:
            blockList.remove("diamond ore")
        if "glowstone" in blockList:
            blockList.remove("glowstone")
    else:
        if "dirt" in blockList:
            blockList.remove("dirt")
        if "log" in blockList:
            blockList.remove("log")
        if "netherrack" in blockList:
            blockList.remove("netherrack")
        if "cobblestone" in blockList:
            blockList.remove("cobblestone")
        
    if q6 == "bright":
        if "stone" in blockList:
            blockList.remove("stone")
        if "iron ore" in blockList:
            blockList.remove("iron ore")
        if "dirt" in blockList:
            blockList.remove("dirt")
        if "log" in blockList:
            blockList.remove("log")
        if "netherrack" in blockList:
            blockList.remove("netherrack")
        if "cobblestone" in blockList:
            blockList.remove("cobblestone")
    else:
        if "diamond ore" in blockList:
            blockList.remove("diamond ore")
        if "glowstone" in blockList:
            blockList.remove("glowstone")
        
    if len(blockList) == 0:
        reply = "No block fits your choices"
    elif len(blockList) > 1:
        reply = "Multiple blocks fit your choices"
    else:
        reply = "Your block was " + blockList[0]
        
    print("hi")
    return render_template('page1.html',response = reply)
    
if __name__=="__main__":
    app.run(debug=True)