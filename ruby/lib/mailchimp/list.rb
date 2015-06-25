class Mailchimp
  class List
    attr_accessor :name, :id, :subscribers
    def initialize(params)
      @name = params["name"]
      @id = params["id"]
      @subscribers = params["stats"]["member_count"]
    end

  end
end
