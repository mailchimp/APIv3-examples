# This example shows a basic GET request to get all account data
require 'awesome_print'
require './lib/mailchimp'

# Do we have an API Key? If so, initialize a new Mailchimp object
if File.exist?('../APIKEY')
  @api_key = File.open('../APIKEY').read.strip
  @mailchimp_client = Mailchimp.new(@api_key)
else
  raise StandardError, "APIKEY file is not present, please read README.md for more instructions"
end

response = @mailchimp_client.account_details

puts "-----\nHEADERS\n"
ap response.headers
puts "\n\n-----\nACCOUNT DETAILS\n"
ap response
