#!/usr/bin/env ruby

class Doofus
	def self.greet
		puts "Hellloooooooo!"
	end
end

# @region ReopenExistingClass
class Doofus
	def self.greet_differently
		greet
		puts "... my friend"
	end
end
# @endregion

Doofus.greet_differently
