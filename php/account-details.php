<?php

    require_once('lib/MailChimp.php');

    if (file_exists('../APIKEY')) {
        $apiKey = file_get_contents('../APIKEY');
        $MailChimp = new MailChimp('apiUser', $apiKey);
    } else {
        throw new Exception('Missing an API key in a file called "APIKEY" in the root folder', 1);
    }

    $response = $MailChimp->accountDetails();
    var_dump($response);

?>