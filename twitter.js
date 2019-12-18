$(window).load(function () {
  var tweets = jQuery(".tweet");
  jQuery(tweets).each(function (t, tweet) {
    var id = jQuery(this).attr('id');
    twttr.widgets.createTweet(
      id, tweet,
      {
        conversation: 'all',    // or all
        cards: 'visible',  // or visible 
        linkColor: '#cc0000', // default is blue
        theme: 'dark'    // or dark
      });
  });
});
