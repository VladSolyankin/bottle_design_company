
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport"
	      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="../static/css/articles.css">
	<title>Design Company</title>
</head>
<header class="articles__header">
	<a href="index.html">
		<img src="../static/images/logo.png" alt="Design Company logo" class="header__logo">
	</a>

	<div class="header__menu">
		<ul class="header__menu-list">
			<li><a href="/home">HOME</a></li>
			<li><a href="/about">ABOUT US</a></li>
			<li><a href="/portfolio">PORTFOLIO</a></li>
			<li><a href="/contacts">CONTACTS</a></li>
			<li><a href="/articles">ARTICLES</a></li>
			<li><a href="/companies">COMPANIES</a></li>
		</ul>
	</div>
</header>
<div class="articles__hero"></div>
<main>
	<div style="flex-direction: row; display: flex">
		<h1 class = "articles_h1">Articles</h1>
		<label class="buttonclassic" style="position: absolute; right: 40px; align-self: center;" for = "add">Add an a article</label>
		
	</div>
	<input type="checkbox" id="add" name = "add" style="display: none"/>
	

	<div class = "addarticlediv">
		<p style="font-size: 40px; text-align: center">Add an article!</p>
		<form style="display: flex; flex-direction: column; align-items: center; width: 500px" action="/articles" method="post" enctype="multipart/form-data">
			<input type="text" name="name" placeholder="Article name"/>
			<textarea type="text" name="desc" placeholder="Description"></textarea>
			<div style="display: flex; flex-direction: row;">
				<label for = "loadimage" class = "buttonclassic">Select image for an article</label>
				<input id = "loadimage" style="margin-left: 5px; width: 100%; color: white; display: none" accept="image/png, image/jpeg" name="img" type="file"/>
				
			</div>
			<input type="text" name="src-link" placeholder="Source link"/>
			<input type="text" name="author" placeholder="Author"/>
			<button type = "submit" class = "buttonclassic">Add</button>
			
		</form>
	</div>
	<p class=error>{{error}}</p>



	<div class="main_articles_div">
		<div class="article_div">
			<img src="../static/images/about-img.jpg" class="article_img"/>
			<h2 class="articles_h2">An article</h2>
			<hr color="white" width="200px">
			<p class="desc">Best article</p>
			<div class="initials_div">
				<p>An article author</p>
				<p style="margin-left: 15px;">16.01.1980</p>
			</div>
		</div>
		%with open("./static/articles.txt") as f:
		%for line in f:
		<div class="article_div">
			<img src= {{line.split("~")[1]}} class="article_img"/>
			<a class="articles_h2" href="{{line.split("~")[3]}}">{{line.split("~")[0]}}</a>
			<hr color="white" width="200px">
			<p class="desc">{{line.split("~")[2]}}</p>
			<div class="initials_div">
				<p>{{line.split("~")[4]}}</p>
				<p style="margin-left: 15px;">{{line.split("~")[5]}}</p>
			</div>
		</div>
		%end


	</div>
	
	

	
	
</main>




<footer>Lab #2<br>GUAP</footer>

</html>