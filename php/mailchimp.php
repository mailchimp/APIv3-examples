<?php

class MailChimpException extends Exception { };

/**
 * Class MailChimp
 */

class MailChimp {

	private $api_uri;
	private $api_user = 'api_v3';
	private $api_key = '';
	private $user_agent = 'API V3 - PHP Sample';

	public function __construct($api_key)
	{
		$domain = explode('-', $api_key)[1];
		$this->api_uri = 'https://' . $domain . '.api.mailchimp.com/3.0';
		$this->api_key = $api_key;
	}

	private function _execute_request($method, $endpoint, Array $payload = [])
	{
		$endpoint = $this->api_uri.$endpoint;

		$ch = curl_init();

		curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
		curl_setopt($ch, CURLOPT_USERPWD, $this->api_user.':'.$this->api_key);
		curl_setopt($ch, CURLOPT_USERAGENT, $this->user_agent);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
		curl_setopt($ch, CURLOPT_TIMEOUT, 10);
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, TRUE);

		switch ($method)
		{
			case 'DELETE':
				curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');
				curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
				break;
			case 'GET':
				$endpoint .= '?' . http_build_query($payload);
				break;
			case 'DELETE':
				$endpoint .= '?' . http_build_query($payload);
				break;
			case 'POST':
				curl_setopt($ch, CURLOPT_POST, TRUE);
				curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
				break;
			case 'PUT':
				curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
				curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
				break;
		}

		curl_setopt($ch, CURLOPT_URL, $endpoint);
		$result = curl_exec($ch);

		return json_decode($result);
	}

	/**
	 * List: Add a new subscriber
	 * @docs http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/
	 * @param array $options
	 * @return mixed
	 * @throws MailChimpException
	 *
	 * Usage Example:
	 * 		$obj->list_add_subscriber([
	 * 			'id_list' => 'ID_LIST',	// Required
	 * 			'email' => 'EMAIL',		// Required
	 * 			'status' => 'STATUS',	// Optional
	 * 			'merge_fields' => [		// Optional
	 * 				'FNAME' => 'NAME',
	 * 				...
	 * 			],
 	 * 		]);
	 *
	 */
	public function list_add_subscriber(Array $options)
	{
		// Check required params
		if ( ! isset($options['id_list']) OR ! isset($options['email']))
		{
			throw new MailChimpException('Parameters not set on '.__METHOD__);
		}

		$endpoint = '/lists/' . $options['id_list'] . '/members/';
		$payload = [
			'email_address' => $options['email'],
			'status' => isset($options['status']) ? $options['status'] : 'pending',
		];
		if (isset($options['merge_fields']) AND $options['merge_fields'])
		{
			$payload['merge_fields'] = $options['merge_fields'];
		}

		return $this->_execute_request('POST', $endpoint, $payload);
	}


	/**
	 * Campaign: Send a campaign
	 * @docs http://developer.mailchimp.com/documentation/mailchimp/reference/campaigns/#action-post_campaigns_campaign_id_actions_send
	 * @param array $options
	 * @return mixed
	 * @throws MailChimpException
	 *
	 * Usage Example:
	 * 		$obj->campaign_send([
	 * 			'id_campaign' => 'ID_CAMPAIGN',	// Required
	 * 		]);
	 *
	 */
	public function campaign_send(Array $options)
	{
		// Check required params
		if ( ! isset($options['id_campaign']))
		{
			throw new MailChimpException('Parameters not set on '.__METHOD__);
		}

		$endpoint = '/campaigns/' . $options['id_campaign'] . '/actions/send/';

		return $this->_execute_request('POST', $endpoint);
	}
}

?>
