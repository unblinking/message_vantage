function showLoad() {$('load').style.display = 'block';}

function hideLoad() {$('load').style.display = 'none';}

function clearTargets()	{
	clearTargetMessage();
	clearTarget1();
	clearTarget2();
	clearTarget3();
	clearTarget4();
	clearTarget5();
	hideLogo();
}

function hideLogo() {$('logo').style.display = 'none';}
function clearTargetMessage()	{$('message').innerHTML = '';}
function clearTarget1()	{$('one').innerHTML = '';}
function clearTarget2()	{$('two').innerHTML = '';}
function clearTarget3()	{$('three').innerHTML = '';}
function clearTarget4()	{$('four').innerHTML = '';}
function clearTarget5()	{$('five').innerHTML = '';}

function CreateMessage1()	{
	var url = 'cgi-bin/mv_create_message_1.cgi';
	var pars = '';
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function CreateMessage2()	{
	var url = 'cgi-bin/mv_create_message_2.cgi';
	var pars = Form.serialize('create_message_1');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function PreviewMessage1()	{
	var url = 'cgi-bin/mv_preview_message_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function PreviewMessage2()	{
	var url = 'cgi-bin/mv_preview_message_2.cgi';
	var pars = Form.serialize('preview_message_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditMessage1()	{
	var url = 'cgi-bin/mv_edit_message_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditMessage2()	{
	var url = 'cgi-bin/mv_edit_message_2.cgi';
	var pars = Form.serialize('edit_message_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteMessage1()	{
	
	var url = 'cgi-bin/mv_delete_message_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteMessage2()	{
	var url = 'cgi-bin/mv_delete_message_2.cgi';
	var pars = Form.serialize('delete_message_1');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function CreateGroup1()	{
	var url = 'cgi-bin/mv_create_group_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function CreateGroup2()	{
	var url = 'cgi-bin/mv_create_group_2.cgi';
	var pars = Form.serialize('create_group_1');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditGroup1()	{
	var url = 'cgi-bin/mv_edit_group_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditGroup2()	{
	var url = 'cgi-bin/mv_edit_group_2.cgi';
	var pars = Form.serialize('edit_group_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditGroup3()	{
	var url = 'cgi-bin/mv_edit_group_3.cgi';
	var pars = Form.serialize('edit_group_2');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteGroup1()	{
	var url = 'cgi-bin/mv_delete_group_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteGroup2()	{
	var url = 'cgi-bin/mv_delete_group_2.cgi';
	var pars = Form.serialize('delete_group_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteGroup3()	{
	var url = 'cgi-bin/mv_delete_group_3.cgi';
	var pars = Form.serialize('delete_group_2');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function CreateSubscriber1()	{
	var url = 'cgi-bin/mv_create_subscriber_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function CreateSubscriber2()	{
	var url = 'cgi-bin/mv_create_subscriber_2.cgi';
	var pars = Form.serialize('create_subscriber_1');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditSubscriber1()	{
	var url = 'cgi-bin/mv_edit_subscriber_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditSubscriber2()	{
	var url = 'cgi-bin/mv_edit_subscriber_2.cgi';
	var pars = Form.serialize('edit_subscriber_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function EditSubscriber3()	{
	var url = 'cgi-bin/mv_edit_subscriber_3.cgi';
	var pars = Form.serialize('edit_subscriber_2');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteSubscriber1()	{
	var url = 'cgi-bin/mv_delete_subscriber_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteSubscriber2()	{
	var url = 'cgi-bin/mv_delete_subscriber_2.cgi';
	var pars = Form.serialize('delete_subscriber_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function DeleteSubscriber3()	{
	var url = 'cgi-bin/mv_delete_subscriber_3.cgi';
	var pars = Form.serialize('delete_subscriber_2');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function SendMessages1()	{
	var url = 'cgi-bin/mv_send_messages_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function SendMessages2()	{
	var url = 'cgi-bin/mv_send_messages_2.cgi';
	var pars = Form.serialize('send_messages_1');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function SendMessages3()	{
	var url = 'cgi-bin/mv_send_messages_3.cgi';
	var pars = Form.serialize('send_messages_2');
	var target = 'message';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function ViewHistory1()	{
	var url = 'cgi-bin/mv_view_message_history_1.cgi';
	var pars = '';
	var target = 'one';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function ViewHistory2()	{
	var url = 'cgi-bin/mv_view_message_history_2.cgi';
	var pars = Form.serialize('view_history_1');
	var target = 'two';
	var myAjax = new Ajax.Updater( target, url, { method: 'post', parameters: pars, onLoading: showLoad, onComplete: hideLoad });
}

function copyToList(from,to)	{
	fromList = $(from);
	toList = $(to);
	var sel = false;
	for (i=0;i<fromList.options.length;i++)	{
		var current = fromList.options[i];
		if (current.selected)	{
			sel = true;
			txt = current.text;
			val = current.value;
			toList.options[toList.length] = new Option(txt,val);
			fromList.options[i] = null;
			i--;
		}
	}
	if (!sel) alert ('Select an option first!');
}

function allSelect(id)	{
  List = $(id);
  if (List.length && List.options[0].value == 'temp') return;
  for (i=0;i<List.length;i++)  {
     List.options[i].selected = true;
  }
}

function allCheck(formname,checkname,thestate){
	var el_collection=eval("document.forms."+formname+"."+checkname)
	for (c=0;c<el_collection.length;c++)
	el_collection[c].checked=thestate
}
