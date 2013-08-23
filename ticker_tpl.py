tpl = '''
<html><head>
			<style type="text/css">
			h1 { color:blue; font-size:64px; }
			input[type=submit] {font-size:48px;}
			input[type=text] {font-size:48px;}
			p {font-size:48px;}
			table { width:100%; }
			td { border:1px solid #000; vertical-align:top; overflow:hidden; font-size:13px; font-family:Verdana,sans-serif; font-weight:bold;}
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
			<table>
			<tr>
			<td colspan=3><input type="text" name="hteam" value="{{hteam}}"></td>
			</tr>
			<tr>
			<td><input type="submit" name="home_u" value="{{home}}"></td>
			<td>:</td>
			<td><input type="submit" name="home_d" value="{{guest}}"></td>
			</tr>
			<tr>
			<td><input type="submit" name="guest_u" value="Guest+"></td>
			<td></td>
			<td><input type="submit" name="guest_d" value="Guest-"></td>
			</tr>
			<tr>
			<td><input type="submit" name="new" value="New"></td>
			<td><input type="submit" name="start" value="Start"></td>
			<td><input type="submit" name="end" value="End"></td>
			</tr>
			
			</table>
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
#	print a
	

