<?php

    require_once('lib/MailChimp.php');
    $apiKeyPath = '../APIKEY';

    if (file_exists($apiKeyPath)) {
        $apiKey = file_get_contents($apiKeyPath);
        $MailChimp = new MailChimp(YOUR_MAILCHIMP_API_USER, $apiKey);
    } else {
        throw new Exception('Missing an API key in a file called "APIKEY" in the root folder', 1);
    }

    $response = $MailChimp->accountDetails();
    var_dump($response);

?>