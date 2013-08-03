tpl = '''
<html><head>
			<style type="text/css">
			h1 { color:blue; font-size:64px; }
			input[type=submit] {font-size:48px;}
			input[type=text] {font-size:48px;}
			p {font-size:48px;}
			</style>
		</head>
<body>
	<h1>Ticker {{mid}}</h1>
		<p><a href="{{mail}}">Mail</a></p>
		<p>
		%for si in mids:
			<a href="/{{si}}">{{si}}</a>
			<a href="/del/{{si}}"> [del]</a>
		%end
		</p>
		<form action="/{{mid}}" method="POST">
			<input type="submit" name="home" value="Home">
			<input type="submit" name="guest" value="Guest">
			<input type="submit" name="new" value="New">
		</form>
	<h1>Output</h1>
		<p>{{home}} : {{guest}}</p>
</body></html>
'''

# write
with open('ticker.tpl','w') as f:
	f.write(tpl)

# verify
with open('ticker.tpl') as f:
	a = f.read()
	print a
	

