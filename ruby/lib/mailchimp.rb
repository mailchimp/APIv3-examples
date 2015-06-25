require 'httparty'

class Mailchimp
  include HTTParty

  def initialize(api_key)
    # Do we have a valid API Key?
    unless api_key =~ /\w+-\w{3}/
      raise StandardError, "Invalid API Key"
    end

    domain = api_key.split('-')[1]
    @auth = {username: 'apikey', password: api_key}

    self.class.base_uri "https://#{domain}.api.mailchimp.com/3.0"
  end

  def account_details
    self.class.get('/', basic_auth: @auth)
  end

end
