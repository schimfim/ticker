tpl = '''
<html><head>

	<script type="text/JavaScript">
		var doReload = true;
		
		function reload() {
		    if (doReload)
		   	 window.location.href='/{{mid}}';
		}
		
		function timedRefresh(t) {
			setTimeout(reload, t);
		}
	</script>
	
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
<body onload="JavaScript:timedRefresh({{refresh}});">
	<h1>Fussi Ticker</h1>
		<form action="/{{mid}}" name="theForm" method="POST">
			<table>
			<tr>
			<td colspan=2 align="center">
			%if running:
				<input type="text" name="hteam" style="background-color:red" value="{{hteam}}" onfocus="doReload=false" onblur="document.theForm.submit()">
			%else:
				<input type="text" name="hteam" value="{{hteam}}" onfocus="doReload=false" onblur="document.theForm.submit()">
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
			%if running:
				<td style="background-color:red">
				<input type="submit" name="start" value="Stop">
				</td>
			%else:
				<td>
				<input type="submit" name="start" value="Start">
				</td>
			%end
			
			<td><input type="submit" name="reset" value="Neu"></td>
			
			</tr>
			</table>
		</form>
		%if not mid:
			<p><a href="{{base_url}}/{{cookie}}">Verwende den Ticker vom letzten Mal</a></p>
		%end
		<p><a href="{{mail}}">Teile diesen Ticker</a></p>
		
</body></html>
'''

# write
with open('ticker.tpl','w') as f:
	f.write(tpl)

# verify
#with open('ticker.tpl') as f:
#	a = f.read()
#	print a
	

