# Regional
Include working code snippets in published documents.

### Example

Consider the following rude ruby trick:

```ruby
# april_fools.rb
class Object
  # @region RenameOldMethod
  alias :nil? :old_nil 
  # @endregion

  def nil?
    (rand > 0.01) ? old_nil : !old_nil
  end
end
```

Running `$ ./regional.py april_fools.rb` would produce the following snippet:

```ruby
# RenameOldMethod.snippet.rb
alias :nil? :old_nil
