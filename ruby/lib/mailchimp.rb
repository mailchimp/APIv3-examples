require 'httparty'

require './lib/mailchimp/list'

class Mailchimp
  include HTTParty
  attr_accessor :lists

  def initialize(api_key)
    # Do we have a valid API Key?
    unless api_key =~ /\w+-\w{3}/
      raise StandardError, "Invalid API Key"
    end

    domain = api_key.split('-')[1]
    @auth = {username: 'apikey', password: api_key}

    self.class.base_uri "https://#{domain}.api.mailchimp.com/3.0"

    @lists = []
  end

  def account_details
    self.class.get('/', basic_auth: @auth)
  end

  def list_details
    response = self.class.get('/lists', basic_auth: @auth, query: {fields: 'lists.id,lists.name,lists.stats.member_count'})
    response["lists"].each {|list| self.lists << Mailchimp::List.new(list)}

    return self.lists
  end


end
