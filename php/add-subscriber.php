<?php

    require_once('lib/MailChimp.php');

    if (file_exists('../APIKEY')) {
        $apiKey = file_get_contents('../APIKEY');
        $MailChimp = new MailChimp('apiUser', $apiKey);
    } else {
        throw new Exception('Missing an API key in a file called "APIKEY" in the root folder', 1);
    }

    // Replace the parameters of the addSubscriber() method by your own ones
    $response = $MailChimp->addSubscriber(YOUR_MAILCHIMP_LIST_ID, SUBSCRIBER_FIRSTNAME, SUBSCRIBER_LASTNAME, SUBSCRIBER_EMAIL);
    var_dump($response);

?>