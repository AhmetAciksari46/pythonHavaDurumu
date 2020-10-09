# pythonHavaDurumu
python kullanarak webden yerel bazlı hava durumu bilgilerini çekme

hatay/iskenderun bölgesinde yaşadığım için websitesinde ki ilgili yeri sizin düzeltmeniz gerekmektedir.

beautiful soap kullanarak hava durumu bilgileri webden çekilmiştir.

***bazı dosyaları nokta atışı çekemedeğim için genel olarak çekip sonrasında split ile parçalayarak faydalı verilere ulaştım. Vaktim olunca bu kısmı düzelteceğim..
alttaki kısım sitenin faydalı bölümü. burayı bölerek istenilen kısımlara erişilmiştir.


<div class="today sevendays">
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/today/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Bu gece</b><span>09 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="2" data-night="true"></span></div>
        <div class="temps"><span>asgari: 22°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(2));</script></span></div>
        <div class="wind"><span class="wind-pixida-big se"><div class="wind-popinfo">125°</div></span><br>23 Km/h</div>
        <div class="extra">Yağış<br><b>0</b> mm</div>
        <div class="hover">
          <div class="title"><b>Bu gece</b><span>09 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="2" data-night="true"></span></div>
          <div class="temps"><span>asgari: 22°C</span></div>
          <div class="info"><span class="extra">Oldukça açık.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/today/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/tomorrow/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Cumartesi</b><span>10 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
        <div class="temps"><b>azami: 31°C</b><span>asgari: 26°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(4));</script></span></div>
        <div class="wind"><span class="wind-pixida-big se"><div class="wind-popinfo">138°</div></span><br>21 Km/h</div>
        <div class="extra">Yağış<br><b>0</b> mm</div>
        <div class="hover">
          <div class="title"><b>Cumartesi</b><span>10 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
          <div class="temps"><b>azami: 31°C</b><span>asgari: 26°C</span></div>
          <div class="info"><span class="extra">Gökyüzü parçalı bulutlu.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/tomorrow/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/day2/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Pazar</b><span>11 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="2"></span></div>
        <div class="temps"><b>azami: 27°C</b><span>asgari: 25°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(2));</script></span></div>
        <div class="wind"><span class="wind-pixida-big wnw"><div class="wind-popinfo">297°</div></span><br>11 Km/h</div>
        <div class="extra">Yağış<br><b>0</b> mm</div>
        <div class="hover">
          <div class="title"><b>Pazar</b><span>11 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="2"></span></div>
          <div class="temps"><b>azami: 27°C</b><span>asgari: 25°C</span></div>
          <div class="info"><span class="extra">Oldukça açık.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/day2/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/day3/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Pazartesi</b><span>12 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
        <div class="temps"><b>azami: 27°C</b><span>asgari: 25°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(4));</script></span></div>
        <div class="wind"><span class="wind-pixida-big nnw"><div class="wind-popinfo">335°</div></span><br>10 Km/h</div>
        <div class="extra">Yağış<br><b>0</b> mm</div>
        <div class="hover">
          <div class="title"><b>Pazartesi</b><span>12 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
          <div class="temps"><b>azami: 27°C</b><span>asgari: 25°C</span></div>
          <div class="info"><span class="extra">Gökyüzü parçalı bulutlu.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/day3/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/day4/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Salı</b><span>13 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
        <div class="temps"><b>azami: 27°C</b><span>asgari: 25°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(4));</script></span></div>
        <div class="wind"><span class="wind-pixida-big w"><div class="wind-popinfo">263°</div></span><br>14 Km/h</div>
        <div class="extra">Yağış<br><b>0</b> mm</div>
        <div class="hover">
          <div class="title"><b>Salı</b><span>13 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
          <div class="temps"><b>azami: 27°C</b><span>asgari: 25°C</span></div>
          <div class="info"><span class="extra">Gökyüzü parçalı bulutlu.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/day4/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/day5/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Çarşamba</b><span>14 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="2"></span></div>
        <div class="temps"><b>azami: 27°C</b><span>asgari: 24°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(2));</script></span></div>
        <div class="wind"><span class="wind-pixida-big w"><div class="wind-popinfo">276°</div></span><br>13 Km/h</div>
        <div class="extra">Yağış<br><b>0,1</b> mm</div>
        <div class="hover">
          <div class="title"><b>Çarşamba</b><span>14 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="2"></span></div>
          <div class="temps"><b>azami: 27°C</b><span>asgari: 24°C</span></div>
          <div class="info"><span class="extra">Oldukça açık.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/day5/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
      <div class="day" onclick="window.location='/havadurumu/iskenderun/daily-forecast/day6/?gid=311111&amp;language=turkish&amp;country=turkey';">
        <div class="title"><b>Perşembe</b><span>15 Eki</span></div>
        <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
        <div class="temps"><b>azami: 27°C</b><span>asgari: 26°C</span></div>
        <div class="pred"><span><script>document.write(Icons.GetDescription(3));</script></span></div>
        <div class="wind"><span class="wind-pixida-big sw"><div class="wind-popinfo">228°</div></span><br>15 Km/h</div>
        <div class="extra">Yağış<br><b>0</b> mm</div>
        <div class="hover">
          <div class="title"><b>Perşembe</b><span>15 Eki</span></div>
          <div class="icon"><span class="wicon w78x73 " data-icon="3"></span></div>
          <div class="temps"><b>azami: 27°C</b><span>asgari: 26°C</span></div>
          <div class="info"><span class="extra">Gökyüzü parçalı bulutlu.</span></div>
          <div class="more"><a href="/havadurumu/iskenderun/hourly-forecast/day6/?gid=311111&amp;language=turkish&amp;country=turkey">Saatlik</a></div>
        </div>
      </div>
    
