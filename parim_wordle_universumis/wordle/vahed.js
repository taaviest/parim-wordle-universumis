<script language="javascript" type="text/javascript">

function fnMoveItems(lstbxFrom,lstbxTo)
{
 var varFromBox = document.all(lstbxFrom);
 var varToBox = document.all(lstbxTo); 
 if ((varFromBox != null) && (varToBox != null)) 
 { 
  if(varFromBox.length < 1) 
  {
   alert('There are no items in the source ListBox');
   return false;
  }
  if(varFromBox.options.selectedIndex == -1) // when no Item is selected the index will be -1

  {
   alert('Please select an Item to move');
   return false;
  }
  while ( varFromBox.options.selectedIndex >= 0 ) 
  { 
   var newOption = new Option(); // Create a new instance of ListItem 

   newOption.text = varFromBox.options[varFromBox.options.selectedIndex].text; 
   newOption.value = varFromBox.options[varFromBox.options.selectedIndex].value; 
   varToBox.options[varToBox.length] = newOption; //Append the item in Target Listbox

   varFromBox.remove(varFromBox.options.selectedIndex); //Remove the item from Source Listbox 

  } 
 }
 return false; 
}
</script>