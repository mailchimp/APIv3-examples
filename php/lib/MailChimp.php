<?php

    class MailChimp {

        function __construct( $apiUser, $apiKey ) {
            $domain = explode('-', $apiKey)[1];

            $this->apiUri = 'https://' . $domain . '.api.mailchimp.com/3.0';
            $this->apiUser = $apiUser;
            $this->auth = $apiUser . ':' . $apiKey;
        }

        private function execRequest( $method, $endpoint, $payload = array() ) {
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $endpoint);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
            curl_setopt($ch, CURLOPT_USERPWD, $this->auth);
            curl_setopt($ch, CURLOPT_USERAGENT, 'apiUser');
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_TIMEOUT, 10);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

            if ($method == 'DELETE') {
              curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');
              curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
            }

            if ($method == 'GET' && !empty($payload)) {
              $endpoint .= '?' . http_build_query($payload);
            }

            if ($method == 'POST') {
              curl_setopt($ch, CURLOPT_POST, TRUE);
              curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
            }

            if ($method == 'PUT') {
              curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
              curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
            }

            $result = curl_exec($ch);

            return json_decode($result);
        }

        public function addSubscriber( $listId, $firstName, $lastName, $email ) {
            $endpoint = $this->apiUri . '/lists/' . $listId . '/members/';

            $payload = array(
                'email_address' => $email,
                'status' => 'pending',
                'merge_fields' => array(
                    'FNAME' => $firstName,
                    'LNAME' => $lastName
                )
            );

            return $this->execRequest('POST', $endpoint, $payload);
        }


        public function accountDetails() {
            $endpoint = $this->apiUri . '/';

            return $this->execRequest('GET', $endpoint);
        }
    }

?>