tpl = '''
<html><head>
	<meta http-equiv="expires" content="10"/>
	<meta http-equiv="refresh" content="10; URL=/{{mid}}" /> 
			<style type="text/css">
			body {background-color:green; font-family:sans-serif}
			h1 { font-size:3cm; text-align:center; background-color:white;}
			input[type=submit] {background-color:transparent; width:100%; color:white; font-size:2cm; border-style:none}
			input[type=text] {font-size:2cm; width:100%; background-color:transparent; color:white}
			p {font-size:48px; align:center;}
			table { width:100%; border-spacing:0px; border-collapse:collapse; table-layout:fixed}
			td { border:10px solid white; vertical-align:center; align:center; overflow:hidden; font-size:3cm; font-weight:bold; background-color:green;}
			input[type=submit].score {color:white; font-size:5cm;}
			</style>
		</head>
<body>
	<h1>Fussi Ticker</h1>
		<form action="/{{mid}}" method="POST">
			<table>
			<tr>
			<td colspan=2 align="center">
			%if running:
				<input type="text" name="hteam" style="background-color:red"; value="{{hteam}}">
			%else:
				<input type="text" name="hteam" value="{{hteam}}">
			%end
			</td>
			</tr>
			<tr style="height:6cm;">
			<td><input class="score" type="submit" name="home_u" value="{{home}}"></td>
			<td><input class="score" type="submit" name="guest_u" value="{{guest}}"></td>
			</tr>
			<tr style="height:2cm;">
			<td><input type="submit" name="home_d" value="-"></td>
			<td><input type="submit" name="guest_d" value="-"></td>
			</tr>
		</table>
		<br>
		<table>
			<tr>
			<td><input type="submit" name="new" value="New"></td>
			<td><input type="submit" name="start" value="Start"></td>
			<td><input type="submit" name="end" value="End"></td>
			</tr>
			
			</table>
		</form>
		<p><a href="{{mail}}">Share this Ticker</a></p>
</body></html>
'''

# write
with open('ticker.tpl','w') as f:
	f.write(tpl)

# verify
with open('ticker.tpl') as f:
	a = f.read()
#	print a
	

