# PHP Example of using the Mailchimp API v3.x

This is a basic example of adding a subscriber ('creating a member' in Mailchimp speak) to a list.

## Prerequisites

You'll need the following to do this:

* Reference the official [Mailchimp API docs on the subject](http://developer.mailchimp.com/documentation/mailchimp/reference/lists/members/#create-post_lists_list_id_members).
* [Get your API key](http://kb.mailchimp.com/integrations/api-integrations/about-api-keys)
* [Get the ID of the list you want to add people into](http://kb.mailchimp.com/integrations/api-integrations/about-api-keys)

## Background

Mailchimp recommends a basic HTTP authentication which we can accomplish by using PHP's cURL library. Pay particular attention to the [CURL_SETOPT](http://php.net/manual/en/function.curl-setopt.php) items, as this can prove particularly difficult to deal with.
