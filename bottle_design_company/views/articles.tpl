
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
		</ul>
	</div>
</header>
<div class="articles__hero"></div>
<main>
	<h1 class = "articles_h1">Articles</h1>
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
		%with open("C:/Users/admin/source/repos/bottle_design_company/bottle_design_company/static/articles.txt") as f:
		%for line in f:
		<div class="article_div">
			<img src= {{line.split("~")[1]}} class="article_img"/>
			<h2 class="articles_h2">{{line.split("~")[0]}}</h2>
			<hr color="white" width="200px">
			<p class="desc">{{line.split("~")[2]}}</p>
			<div class="initials_div">
				<p>{{line.split("~")[3]}}</p>
				<p style="margin-left: 15px;">{{line.split("~")[4]}}</p>
			</div>
		</div>
		%end


	</div>
	
	

	<div style="margin-top: 50px; flex-direction: column;">
		<p style="font-size: 40px;">Add a article!</p>
		<form style="display: flex; flex-direction: column;" action="/articles" method="post" enctype="multipart/form-data">
			<input type="text" name="name" placeholder="Article name"/>
			<input type="text" name="desc" placeholder="Description"/>
			<div style="display: flex; flex-direction: row;">
				<p style="align-self: center;">Image</p>
				
			</div>
			<input style="margin-left: 5px;" name="img" type="file"/>
			<input type="text" name="author" placeholder="Author"/>
			<button type = "submit">Add</button>
			
		</form>
	</div>
	
</main>




<footer>Lab #2<br>GUAP</footer>

</html>