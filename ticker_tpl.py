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
			<input type="text" name="hteam" value="{{hteam}}">
			<input type="submit" name="home_u" value="Home+">
			<input type="submit" name="home_d" value="Home-">
			<input type="submit" name="guest_u" value="Guest+">
			<input type="submit" name="guest_d" value="Guest-">
			<input type="submit" name="new" value="New">
			<input type="submit" name="start" value="Start">
			<input type="submit" name="end" value="End">
		</form>
	<h1>Output</h1>
	%if running:
		<p>Running</p>
	%else:
		<p>Game over</p>
	%end
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
	

