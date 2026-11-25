function doGet() { return HtmlService.createHtmlOutputFromFile('Index').setTitle('Salon V2 — scaffold'); }
function rpc(request) { return {ok:false,error:{code:'NOT_CONFIGURED',message:'Authentication and domain services are not implemented.'}}; }
