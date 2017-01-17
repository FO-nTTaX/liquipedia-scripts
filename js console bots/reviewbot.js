var wiki = 'heroes';
var pages = [
'Template:TeamShort/burning rage',
'Template:Team/burning rage',
'Template:Team2/burning rage',
'Template:Team2Short/burning rage',
'Template:TeamBracket/burning rage',
'Template:TeamIcon/burning rage',
'Template:TeamPart/burning rage',
'Template:Team/imperium',
'Template:TeamShort/imperium',
'Template:Team2/imperium',
'Template:Team2Short/imperium',
'Template:TeamBracket/imperium',
'Template:TeamIcon/imperium',
'Template:TeamPart/imperium',
'Template:TeamPage/imperium',
'Template:TeamPart/team up',
];
function dopage(i, max) {
	if(i + 1 > max) {
		return;
	}
	$.getJSON('http://wiki.teamliquid.net/' + wiki + '/api.php?action=query&meta=tokens&format=json', function(data) {
		var csrftoken = data.query.tokens.csrftoken;
		$.getJSON('http://wiki.teamliquid.net/' + wiki + '/api.php?action=query&prop=revisions&titles=' + mw.util.rawurlencode(pages[i]) + '&rvprop=ids&format=json', function(data) {
			var revid;
			$.each(data.query.pages, function(index, element) {
				var revid = element.revisions[0].revid;
				$.post('http://wiki.teamliquid.net/' + wiki + '/api.php?action=review&revid=' + revid + '&flag_accuracy=1&comment=team%20template', {'token': csrftoken}, function(data) {null;});
				console.log('Title: ' + pages[i]);
				console.log('Token: ' + csrftoken);
				console.log('Revid: ' + revid);
				dopage(i + 1, max);
			});
		});
		
	});
}
dopage(0, pages.length);
