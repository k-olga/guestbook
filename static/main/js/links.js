onload = function ()
{
for (var lnk = document.getElementsByTagName('a'), j = 0; j < lnk.length; j++)
if (lnk[j].href == document.URL || document.URL.indexOf(lnk[j].href) != -1) {
 lnk[j].className += ' act';
}
}
