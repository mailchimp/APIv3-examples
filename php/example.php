<?php
require_once(__DIR__.'/mailchimp.php');

// Init mailchimp
$mailchimp = new MailChimp('YOUR API KEY');

$reply = $mailchimp->list_add_subscriber([
	'id_list' => 'ID_LIST',
	'email' => 'EMAIL',
	'status' => 'STATUS',
	'merge_fields' => [
		'FNAME' => 'FIRST NAME',
	],
]);

echo '<pre>';
print_r($reply);
echo '</pre>';
