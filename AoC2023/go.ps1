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

#$realdataurl
#return 0

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
$testdata | Out-File $dest -Encoding ASCII


$dest = $newpath + "/real.txt"
$session = [Microsoft.Powershell.Commands.WebRequestSession]::new()
$cookie = [System.Net.Cookie]::new('session', $sessioncookie)
$session.Cookies.Add('https://adventofcode.com', $cookie)
iwr -uri $realdataurl -websession $session -outfile $dest -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

cd $newpath
ls

#$wc = New-Object System.Net.WebClient
#$wc.Headers.Add([System.Net.HttpRequestHeader]::UserAgent, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition beta)")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::Accept, "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::AcceptEncoding, "gzip, deflate, br")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::AcceptLanguage, "en-US,en;q=0.9")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::CacheControl, "max-age=0")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::Connection, "keep-alive")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::Host, "adventofcode.com")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "_ga=GA1.2.1782177736.1701406672; _gid=GA1.2.484692841.1701639535; session=53616c7465645f5fe98070d8f531b8e0df52df6a3512565a9e16b3acfa75b45ad67053b26b84e107eab252bd470515210db3066eb3fac3ddad7e9003846b67c5; _ga_MHSNPJKWC7=GS1.2.1701659747.6.1.1701659751.0.0.0")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::UserAgent, "github.com/jakeydo/AoC/blob/main/AoC2023/go.ps1")# by jakespencer@gmail.com")
#$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "session=53616c7465645f5f7e5596b8a16a86ad030259ec181610b7cd36bb90ad72d154183c633ec7bbfcc9f62f2bde6f728fbaf208fb4651a4071b653439cbc1581ff9")
#$wc.DownloadFile($realdataurl, $dest)