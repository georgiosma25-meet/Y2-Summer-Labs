def create_youtube_videos(title, description): 
	myDict = {"title": title , "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtag": []} 

	return myDict 

 
 
def like (myDict) : 
	if "likes" in myDict : 
		myDict["likes"]+=1  
	return myDict 
 
def dislike (myDict) : 
	if "dislikes" in myDict : 
		myDict["dislikes"]+=1 
		return myDict 

username = input ("Username: " ) 
comment_text = input("Comment: ") 
def add_comment (myDict, username, comment_text) : 
	myDict["comments"][username]= comment_text 
	return myDict  
youtube_dict = create_youtube_videos("Sari's youtube video!", "My first video") 

while youtube_dict["likes"] < 495:
	youtube_dict["likes"] +=1 

while len(youtube_dict["hashtag"]) < 5 : 
	youtube_dict["hashtag"].append(input("Hashtag: "))

print(youtube_dict)