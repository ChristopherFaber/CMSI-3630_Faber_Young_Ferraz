from BinaryTreeNode import BinaryTreeNode

   
def  pre_order_printer( current_node ):
      if( current_node == None ):
            return
      print( "[" , current_node.get_data() , "]" )
      pre_order_printer( current_node.get_child( "L" ) )
      pre_order_printer( current_node.get_child( "R" ) )

def post_order_printer( current_node ):
      if current_node == None:
         return
      post_order_printer( current_node.get_child( "L" ) )
      post_order_printer( current_node.get_child( "R" ) )
      print( "[" , current_node.get_data() , "]" )

def in_order_printer( current_node ):
      if current_node == None:
         return
      in_order_printer( current_node.get_child( "L" ) )
      print( "[" , current_node.get_data() , "]" )
      in_order_printer( current_node.get_child( "R" ) )
      
def pressReturn():
      input( "        [press 'enter' to see the result]... <=" )

def main():
      root = BinaryTreeNode( 0 )
      root.add_child( 1, "L" )
      root.add_child( 2, "R" )
      one = root.get_child( "L" )
      two = root.get_child( "R" )
      one.add_child( 3, "L" )
      one.add_child( 4, "R" )
      two.add_child( 5, "L" )
      two.add_child( 6, "R" )
      six = two.get_child( "R" )
      six.add_child( 7, "L" )
      six.add_child( 8, "R" )
      print( "one left: ", one.get_child("L").get_data() )

      print( "\n\n  ==== the tree looks like this [sorta]: \n\n" )
      print( "                  (", root.get_data(), ")" )
      print( "                   / \\" )
      print( "                  /   \\" )
      print( "                 /     \\" )
      print( "                /       \\" )
      print( "               /         \\" )
      print( "              /           \\" )
      print( "             /             \\" )
      print( "          (", one.get_data(), ")           (", two.get_data(), ")" )
      print( "           / \\             / \\" )
      print( "          /   \\           /   \\" )
      print( "         /     \\         /     \\" )
      print( "        /       \\       /       \\" )
      print( "     (", one.get_child("L").get_data(), ")", end="" )
      print( "     (", one.get_child("R").get_data(), ")", end="" )
      print( " (", two.get_child("L").get_data(), ")", end="" )
      print( "     (", two.get_child("R").get_data(), ")" )
      print( "                                / \\" )
      print( "                               /   \\" )
      print( "                            (", six.get_child("L").get_data(), ")", end="" )
      print( " (", six.get_child("R").get_data(), ")" )
      pre_order_printer(root)
      print('\n')
      post_order_printer(root)
      print('\n')
      in_order_printer( root )
   # run the code above
   #  to print out the tree values
main()
