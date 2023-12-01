$time = get-date
$time = [TimeZoneInfo]::ConvertTimeBySystemTimeZoneId($time, 'Eastern Standard Time')
$day = get-date $time -Format "dd"
#$day = "05"
$daynozero = $day.trimstart('0')
$year = get-date $time -Format "yyyy"
#$year = "2022"
$newfolder = "/AoC" + $year + "d" + $day
$basepath = Convert-Path .
$newpath = $basepath + $newfolder

New-Item -Path $newpath -ItemType Directory

Copy-Item -Path "template.py" -Destination ($newpath + "/main.py")

$testdataurl = "https://adventofcode.com/" + $year + "/day/" + $daynozero
$realdataurl = "https://adventofcode.com/" + $year + "/day/" + $daynozero + "/input"

#download and save test data
$dest = $newpath + "/test.txt"

$sessioncookie = get-content session.txt
$wc = New-Object System.Net.WebClient
$wc.Headers.Add([System.Net.HttpRequestHeader]::UserAgent, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, $sessioncookie)
$wc.DownloadFile($testdataurl, $dest)
$html = new-object -com "HTMLFile"
$content = get-content -path $dest -raw
$newcontent = $content.replace('<pre>','<pre class="jakeydo">')
$newcontent = $newcontent.replace('<p>','<p class="jakeydo">')
$newhtml = new-object -com "HTMLFile"
$newhtml.IHTMLDocument2_write($newcontent)
$js = $newhtml.body.getelementsbyclassname('jakeydo')
$testdataindex = -1
for($i=0; $i -lt $js.Length; $i++){
	if($js[$i].innertext -like "*or example*"){
		$testdataindex = $i+1
	}
}
$testdata = $js[$testdataindex].innerText
$testdata | Out-File $dest


$dest = $newpath + "/real.txt"
$wc = New-Object System.Net.WebClient
$wc.Headers.Add([System.Net.HttpRequestHeader]::UserAgent, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "session=53616c7465645f5f7e5596b8a16a86ad030259ec181610b7cd36bb90ad72d154183c633ec7bbfcc9f62f2bde6f728fbaf208fb4651a4071b653439cbc1581ff9")
$wc.DownloadFile($realdataurl, $dest)