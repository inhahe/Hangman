<?php
  $wordsfile = fopen("d:\\mypage\\words.json", "r");
  $words = json_decode(fread($wordsfile, filesize("d:\\mypage\\words.json")));
  fclose($wordsfile);
  if($_GET["function"]=="getwordlength")
  {
    $word = array_rand($words);
    echo strlen($word);
  }
  else if($_GET["function"]="getpositions")
  {
    $mask = $_GET["mask"];
    $usedletters = $_GET["usedletters"];
    $letter = $_GET["letter"];
    $pattern = "^/" . preg_replace("/_/", $mask, ".") . "$/";
    $matchingwords = array();
    foreach($words as $word)
    {
      if(preg_match($pattern, $word)===0)
      {
        $hasletter = false;
        foreach(str_split($usedletters) as $usedletter) 
        {
          if(strpos($word, $usedletter)!==false) 
          {
            $hasletter = true;
          }
        }
        if(!$hasletter) 
        {
          array_push($matchingwords, $word);
        }
      }  
    }
    $lettercountwords = array();
    foreach($matchingwords as $matchingword) 
    {
      array_push($lettercountwords, array(preg_match_all("/" . $letter . "/", $matchingword), $matchingword));
    }
    sort($lettercountwords);
    $firstlettercount = $lettercounts[0][0];
    $candidates = array();
    foreach($lettercountwords as $lettercountword) 
    {
      if($lettercountword[0]<=firstlettercount)
      {
        array_push($candidates, $lettercountword);
      }
      else 
      {
        break;
      }
    }
    $candidate = array_rand($candidates);
    $c = preg_match_all("/" . $letter . "/", $candidate, $matches, PREG_OFFSET_CAPTURE);
    if($c==0) 
    { 
      echo "None";
    }
	  else 
	  {
      foreach($matches as $match)
      {
        echo $match[0][1] . ";";
      }
    }	  
  }
  else 
  {
    echo "else";
	}


?>
