def get_rounded_attr(feature, attribute_name, decimals=2):
  """
  Get feature attribute value rounded

  Args:
    feature: QgsFeature object.
    attribute_name: Attribute name.
    decimals: number of decimals to be rounded. Default is 2.

  Returns:
     Attribute value rounded or original value if is not numeric. None if does not exist.
  """
  if attribute_name in feature.fields().names():
    val = feature[attribute_name]   
    if val is not None:        
      try:
        rounded_val = round(float(val), decimals)
        return rounded_val
      except Exception:
        #not numeric value
        return val
    else:
      return None 
  else:
    return None