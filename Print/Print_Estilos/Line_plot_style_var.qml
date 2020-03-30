<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" readOnly="0" simplifyLocal="1" simplifyDrawingTol="1" version="3.4.4-Madeira" styleCategories="AllStyleCategories" maxScale="100000" minScale="1e+08" simplifyAlgorithm="0" simplifyDrawingHints="1" simplifyMaxScale="1" labelsEnabled="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" symbollevels="0" type="RuleRenderer">
    <rules key="{7b6772ff-b392-462e-910b-bc97815c9341}">
      <rule filter=" &quot;L&quot; &lt;> 0" key="{89fa5778-836a-4f4c-8b63-e9f38d289fe2}" symbol="0"/>
      <rule filter=" &quot;Caida_p2&quot; ='D'" key="{97cbed74-e7cf-4194-8afd-bb33570d294a}" symbol="1"/>
      <rule filter=" &quot;Caida_p2_h&quot;   > 0 and   &quot;Caida_p2&quot;   = 'TC'" key="{a324e7fc-3afb-48c8-86ba-ac3b5a893d55}" symbol="2"/>
    </rules>
    <symbols>
      <symbol alpha="1" name="0" clip_to_extent="1" type="line" force_rhr="0">
        <layer pass="0" locked="0" enabled="1" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="4,0,241,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.5" k="line_width"/>
          <prop v="MapUnit" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer pass="1" locked="0" enabled="1" class="MarkerLine">
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="vertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" name="@0@1" clip_to_extent="1" type="marker" force_rhr="0">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="0,0,0,0" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="170,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.7" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MapUnit" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="6" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MapUnit" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer pass="2" locked="0" enabled="1" class="MarkerLine">
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="centralpoint" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" name="@0@2" clip_to_extent="1" type="marker" force_rhr="0">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="4,0,241,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="arrowhead" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MapUnit" k="offset_unit"/>
              <prop v="67,67,67,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="1.2" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MapUnit" k="outline_width_unit"/>
              <prop v="area" k="scale_method"/>
              <prop v="7" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MapUnit" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties" type="Map">
                    <Option name="name" type="Map">
                      <Option value="false" name="active" type="bool"/>
                      <Option value="COTAF" name="field" type="QString"/>
                      <Option value="2" name="type" type="int"/>
                    </Option>
                  </Option>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" name="1" clip_to_extent="1" type="line" force_rhr="0">
        <layer pass="0" locked="0" enabled="1" class="MarkerLine">
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="lastvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" name="@1@0" clip_to_extent="1" type="marker" force_rhr="0">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="4,0,241,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="-6,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MapUnit" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.5" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MapUnit" k="outline_width_unit"/>
              <prop v="area" k="scale_method"/>
              <prop v="3" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MapUnit" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" name="2" clip_to_extent="1" type="line" force_rhr="0">
        <layer pass="0" locked="0" enabled="1" class="MarkerLine">
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MM" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MM" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="lastvertex" k="placement"/>
          <prop v="0" k="ring_filter"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol alpha="1" name="@2@0" clip_to_extent="1" type="marker" force_rhr="0">
            <layer pass="0" locked="0" enabled="1" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="255,0,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="-6,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MapUnit" k="offset_unit"/>
              <prop v="0,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.5" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MapUnit" k="outline_width_unit"/>
              <prop v="area" k="scale_method"/>
              <prop v="3" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MapUnit" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{c4bd6813-3ead-45ad-9da4-28c7ee510c4c}">
      <rule filter=" &quot;Caida_p2_h&quot; =0 or  &quot;Caida_p2_h&quot;  is NULL" key="{bb13694a-108a-43af-a087-8d1375a6ddf5}">
        <settings>
          <text-style blendMode="0" fontSize="8.25" fontWeight="50" fontStrikeout="0" textColor="0,0,0,255" fieldName="   &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xa;     ''  || '\n' ||&#xa;     'Ø' ||   &quot;DN&quot;    || '\n' || &#xa;        &quot;S&quot;  " fontItalic="0" previewBkgrdColor="#ffffff" namedStyle="Normal" fontLetterSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontCapitals="0" fontFamily="MS Shell Dlg 2" fontWordSpacing="0" fontSizeUnit="Point" isExpression="1" multilineHeight="1" useSubstitutions="0" textOpacity="1" fontUnderline="0">
            <text-buffer bufferSize="0.7" bufferJoinStyle="64" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferColor="255,255,255,255" bufferBlendMode="0" bufferSizeUnits="MM" bufferDraw="1" bufferNoFill="0"/>
            <background shapeBorderColor="128,128,128,255" shapeRotationType="0" shapeSizeType="0" shapeFillColor="255,255,255,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOffsetX="0" shapeRadiiUnit="MM" shapeOpacity="1" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeOffsetY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeRadiiX="0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBlendMode="0" shapeSVGFile="" shapeBorderWidth="0" shapeRotation="0"/>
            <shadow shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOffsetUnit="MM" shadowOpacity="0.7" shadowScale="100" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadius="1.5" shadowBlendMode="6"/>
            <substitutions/>
          </text-style>
          <text-format leftDirectionSymbol="&lt;" wrapChar="" formatNumbers="0" reverseDirectionSymbol="0" multilineAlign="1" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" decimals="3" rightDirectionSymbol=">" autoWrapLength="0" plussign="0" placeDirectionSymbol="0"/>
          <placement centroidWhole="0" repeatDistanceUnits="MM" rotationAngle="0" placementFlags="9" distUnits="MM" placement="2" offsetUnits="MapUnit" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" priority="5" repeatDistance="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" fitInPolygonOnly="0" xOffset="0" maxCurvedCharAngleOut="-20" centroidInside="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" yOffset="0" maxCurvedCharAngleIn="20" offsetType="0"/>
          <rendering labelPerPart="0" maxNumLabels="2000" limitNumLabels="0" obstacle="1" displayAll="0" mergeLines="0" scaleVisibility="1" scaleMax="4000" fontLimitPixelSize="0" obstacleType="0" drawLabels="1" upsidedownLabels="0" minFeatureSize="0" zIndex="0" obstacleFactor="1" fontMaxPixelSize="10000" scaleMin="1" fontMinPixelSize="3"/>
          <dd_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule filter=" &quot;Caida_p2_h&quot;  &lt;>0 and  &quot;Caida_p2&quot;  ='TC'" key="{42f0326d-c7fd-46c4-b0e8-a8e377f33df7}">
        <settings>
          <text-style blendMode="0" fontSize="8.25" fontWeight="50" fontStrikeout="0" textColor="0,0,0,255" fieldName="    &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xd;&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xd;&#xa;     ''  || '\n' ||&#xd;&#xa;&#x9;  ''  || '\n' ||&#xd;&#xa;      'Ø' ||   &quot;DN&quot;    || '\n' || &#xd;&#xa;        &quot;S&quot;  || '\n' || &#xd;&#xa;&#x9;&#x9; &quot;Caida_p2&quot;   || ' '||   &quot;Caida_p2_h&quot;" fontItalic="0" previewBkgrdColor="#ffffff" namedStyle="Normal" fontLetterSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontCapitals="0" fontFamily="MS Shell Dlg 2" fontWordSpacing="0" fontSizeUnit="Point" isExpression="1" multilineHeight="1" useSubstitutions="0" textOpacity="1" fontUnderline="0">
            <text-buffer bufferSize="0.7" bufferJoinStyle="64" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferColor="255,255,255,255" bufferBlendMode="0" bufferSizeUnits="MM" bufferDraw="1" bufferNoFill="0"/>
            <background shapeBorderColor="128,128,128,255" shapeRotationType="0" shapeSizeType="0" shapeFillColor="255,255,255,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOffsetX="0" shapeRadiiUnit="MM" shapeOpacity="1" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeOffsetY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeRadiiX="0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBlendMode="0" shapeSVGFile="" shapeBorderWidth="0" shapeRotation="0"/>
            <shadow shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOffsetUnit="MM" shadowOpacity="0.7" shadowScale="100" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadius="1.5" shadowBlendMode="6"/>
            <substitutions/>
          </text-style>
          <text-format leftDirectionSymbol="&lt;" wrapChar="" formatNumbers="0" reverseDirectionSymbol="0" multilineAlign="1" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" decimals="3" rightDirectionSymbol=">" autoWrapLength="0" plussign="0" placeDirectionSymbol="0"/>
          <placement centroidWhole="0" repeatDistanceUnits="MM" rotationAngle="0" placementFlags="9" distUnits="MM" placement="2" offsetUnits="MapUnit" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" priority="5" repeatDistance="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" fitInPolygonOnly="0" xOffset="0" maxCurvedCharAngleOut="-20" centroidInside="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" yOffset="0" maxCurvedCharAngleIn="20" offsetType="0"/>
          <rendering labelPerPart="0" maxNumLabels="2000" limitNumLabels="0" obstacle="1" displayAll="0" mergeLines="0" scaleVisibility="1" scaleMax="4000" fontLimitPixelSize="0" obstacleType="0" drawLabels="1" upsidedownLabels="0" minFeatureSize="0" zIndex="0" obstacleFactor="1" fontMaxPixelSize="10000" scaleMin="1" fontMinPixelSize="3"/>
          <dd_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule filter=" &quot;Caida_p2&quot; ='D' and  &quot;Caida_p2_h&quot; &lt;>  '0.00' " key="{ad9de7ff-6826-4090-8926-99a52ff6c3eb}">
        <settings>
          <text-style blendMode="0" fontSize="8.25" fontWeight="50" fontStrikeout="0" textColor="0,0,0,255" fieldName="    &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xd;&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xd;&#xa;     ''  || '\n' ||&#xd;&#xa;&#x9;  ''  || '\n' ||&#xd;&#xa;      'Ø' ||   &quot;DN&quot;    || '\n' || &#xd;&#xa;        &quot;S&quot;  || '\n' || &#xd;&#xa;&#x9;&#x9;  'D'   || ' '||  &quot;Caida_p2_h&quot;" fontItalic="0" previewBkgrdColor="#ffffff" namedStyle="Normal" fontLetterSpacing="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontCapitals="0" fontFamily="MS Shell Dlg 2" fontWordSpacing="0" fontSizeUnit="Point" isExpression="1" multilineHeight="1" useSubstitutions="0" textOpacity="1" fontUnderline="0">
            <text-buffer bufferSize="0.7" bufferJoinStyle="64" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferColor="255,255,255,255" bufferBlendMode="0" bufferSizeUnits="MM" bufferDraw="1" bufferNoFill="0"/>
            <background shapeBorderColor="128,128,128,255" shapeRotationType="0" shapeSizeType="0" shapeFillColor="255,255,255,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOffsetX="0" shapeRadiiUnit="MM" shapeOpacity="1" shapeRadiiY="0" shapeBorderWidthUnit="MM" shapeSizeX="0" shapeOffsetY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeRadiiX="0" shapeOffsetUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeDraw="0" shapeType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="MM" shapeBlendMode="0" shapeSVGFile="" shapeBorderWidth="0" shapeRotation="0"/>
            <shadow shadowRadiusUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowOffsetUnit="MM" shadowOpacity="0.7" shadowScale="100" shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowOffsetGlobal="1" shadowRadius="1.5" shadowBlendMode="6"/>
            <substitutions/>
          </text-style>
          <text-format leftDirectionSymbol="&lt;" wrapChar="" formatNumbers="0" reverseDirectionSymbol="0" multilineAlign="2" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" decimals="3" rightDirectionSymbol=">" autoWrapLength="0" plussign="0" placeDirectionSymbol="0"/>
          <placement centroidWhole="0" repeatDistanceUnits="MM" rotationAngle="0" placementFlags="9" distUnits="MM" placement="2" offsetUnits="MapUnit" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" quadOffset="4" priority="5" repeatDistance="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" fitInPolygonOnly="0" xOffset="0" maxCurvedCharAngleOut="-20" centroidInside="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" yOffset="0" maxCurvedCharAngleIn="20" offsetType="0"/>
          <rendering labelPerPart="0" maxNumLabels="2000" limitNumLabels="0" obstacle="1" displayAll="0" mergeLines="0" scaleVisibility="1" scaleMax="4000" fontLimitPixelSize="0" obstacleType="0" drawLabels="1" upsidedownLabels="0" minFeatureSize="0" zIndex="0" obstacleFactor="1" fontMaxPixelSize="10000" scaleMin="1" fontMinPixelSize="3"/>
          <dd_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="false" key="labeling/addDirectionSymbol"/>
    <property value="0" key="labeling/angleOffset"/>
    <property value="0" key="labeling/blendMode"/>
    <property value="0" key="labeling/bufferBlendMode"/>
    <property value="255" key="labeling/bufferColorA"/>
    <property value="255" key="labeling/bufferColorB"/>
    <property value="255" key="labeling/bufferColorG"/>
    <property value="255" key="labeling/bufferColorR"/>
    <property value="true" key="labeling/bufferDraw"/>
    <property value="64" key="labeling/bufferJoinStyle"/>
    <property value="false" key="labeling/bufferNoFill"/>
    <property value="1" key="labeling/bufferSize"/>
    <property value="true" key="labeling/bufferSizeInMapUnits"/>
    <property value="0" key="labeling/bufferSizeMapUnitMaxScale"/>
    <property value="0" key="labeling/bufferSizeMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/bufferSizeMapUnitScale"/>
    <property value="50" key="labeling/bufferTransp"/>
    <property value="false" key="labeling/centroidInside"/>
    <property value="false" key="labeling/centroidWhole"/>
    <property value="3" key="labeling/decimals"/>
    <property value="false" key="labeling/displayAll"/>
    <property value="0" key="labeling/dist"/>
    <property value="false" key="labeling/distInMapUnits"/>
    <property value="0" key="labeling/distMapUnitMaxScale"/>
    <property value="0" key="labeling/distMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/distMapUnitScale"/>
    <property value="true" key="labeling/drawLabels"/>
    <property value="true" key="labeling/enabled"/>
    <property value="  &quot;TRM&quot; ||  '\n'  ||&#xa;    &quot;EXT&quot;   || 'm'  ||  '\n'  ||&#xa;    ''  || '\n' || &#xa;     'Ø' ||  &quot;DIAM&quot;   || '\n' || &#xa;       &quot;DECLIVIDADE&quot;  ||  '\n'  || &#xd;&#xa;&#x9;&#x9; &quot;DISPOSIT&quot;  ||  &quot;ALTURA TQ&quot; " key="labeling/fieldName"/>
    <property value="false" key="labeling/fitInPolygonOnly"/>
    <property value="0" key="labeling/fontCapitals"/>
    <property value="MS Shell Dlg 2" key="labeling/fontFamily"/>
    <property value="false" key="labeling/fontItalic"/>
    <property value="0" key="labeling/fontLetterSpacing"/>
    <property value="false" key="labeling/fontLimitPixelSize"/>
    <property value="10000" key="labeling/fontMaxPixelSize"/>
    <property value="3" key="labeling/fontMinPixelSize"/>
    <property value="8.25" key="labeling/fontSize"/>
    <property value="false" key="labeling/fontSizeInMapUnits"/>
    <property value="0" key="labeling/fontSizeMapUnitMaxScale"/>
    <property value="0" key="labeling/fontSizeMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/fontSizeMapUnitScale"/>
    <property value="false" key="labeling/fontStrikeout"/>
    <property value="false" key="labeling/fontUnderline"/>
    <property value="50" key="labeling/fontWeight"/>
    <property value="0" key="labeling/fontWordSpacing"/>
    <property value="false" key="labeling/formatNumbers"/>
    <property value="true" key="labeling/isExpression"/>
    <property value="true" key="labeling/labelOffsetInMapUnits"/>
    <property value="0" key="labeling/labelOffsetMapUnitMaxScale"/>
    <property value="0" key="labeling/labelOffsetMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/labelOffsetMapUnitScale"/>
    <property value="false" key="labeling/labelPerPart"/>
    <property value="&lt;" key="labeling/leftDirectionSymbol"/>
    <property value="false" key="labeling/limitNumLabels"/>
    <property value="20" key="labeling/maxCurvedCharAngleIn"/>
    <property value="-20" key="labeling/maxCurvedCharAngleOut"/>
    <property value="2000" key="labeling/maxNumLabels"/>
    <property value="false" key="labeling/mergeLines"/>
    <property value="0" key="labeling/minFeatureSize"/>
    <property value="1" key="labeling/multilineAlign"/>
    <property value="1" key="labeling/multilineHeight"/>
    <property value="Normal" key="labeling/namedStyle"/>
    <property value="true" key="labeling/obstacle"/>
    <property value="1" key="labeling/obstacleFactor"/>
    <property value="0" key="labeling/obstacleType"/>
    <property value="0" key="labeling/offsetType"/>
    <property value="0" key="labeling/placeDirectionSymbol"/>
    <property value="2" key="labeling/placement"/>
    <property value="9" key="labeling/placementFlags"/>
    <property value="false" key="labeling/plussign"/>
    <property value="TR,TL,BR,BL,R,L,TSR,BSR" key="labeling/predefinedPositionOrder"/>
    <property value="true" key="labeling/preserveRotation"/>
    <property value="#ffffff" key="labeling/previewBkgrdColor"/>
    <property value="5" key="labeling/priority"/>
    <property value="4" key="labeling/quadOffset"/>
    <property value="0" key="labeling/repeatDistance"/>
    <property value="0" key="labeling/repeatDistanceMapUnitMaxScale"/>
    <property value="0" key="labeling/repeatDistanceMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/repeatDistanceMapUnitScale"/>
    <property value="1" key="labeling/repeatDistanceUnit"/>
    <property value="false" key="labeling/reverseDirectionSymbol"/>
    <property value=">" key="labeling/rightDirectionSymbol"/>
    <property value="4000" key="labeling/scaleMax"/>
    <property value="1" key="labeling/scaleMin"/>
    <property value="true" key="labeling/scaleVisibility"/>
    <property value="6" key="labeling/shadowBlendMode"/>
    <property value="0" key="labeling/shadowColorB"/>
    <property value="0" key="labeling/shadowColorG"/>
    <property value="0" key="labeling/shadowColorR"/>
    <property value="false" key="labeling/shadowDraw"/>
    <property value="135" key="labeling/shadowOffsetAngle"/>
    <property value="1" key="labeling/shadowOffsetDist"/>
    <property value="true" key="labeling/shadowOffsetGlobal"/>
    <property value="0" key="labeling/shadowOffsetMapUnitMaxScale"/>
    <property value="0" key="labeling/shadowOffsetMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/shadowOffsetMapUnitScale"/>
    <property value="1" key="labeling/shadowOffsetUnits"/>
    <property value="1.5" key="labeling/shadowRadius"/>
    <property value="false" key="labeling/shadowRadiusAlphaOnly"/>
    <property value="0" key="labeling/shadowRadiusMapUnitMaxScale"/>
    <property value="0" key="labeling/shadowRadiusMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/shadowRadiusMapUnitScale"/>
    <property value="1" key="labeling/shadowRadiusUnits"/>
    <property value="100" key="labeling/shadowScale"/>
    <property value="30" key="labeling/shadowTransparency"/>
    <property value="0" key="labeling/shadowUnder"/>
    <property value="0" key="labeling/shapeBlendMode"/>
    <property value="255" key="labeling/shapeBorderColorA"/>
    <property value="128" key="labeling/shapeBorderColorB"/>
    <property value="128" key="labeling/shapeBorderColorG"/>
    <property value="128" key="labeling/shapeBorderColorR"/>
    <property value="0" key="labeling/shapeBorderWidth"/>
    <property value="0" key="labeling/shapeBorderWidthMapUnitMaxScale"/>
    <property value="0" key="labeling/shapeBorderWidthMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/shapeBorderWidthMapUnitScale"/>
    <property value="1" key="labeling/shapeBorderWidthUnits"/>
    <property value="false" key="labeling/shapeDraw"/>
    <property value="255" key="labeling/shapeFillColorA"/>
    <property value="255" key="labeling/shapeFillColorB"/>
    <property value="255" key="labeling/shapeFillColorG"/>
    <property value="255" key="labeling/shapeFillColorR"/>
    <property value="64" key="labeling/shapeJoinStyle"/>
    <property value="0" key="labeling/shapeOffsetMapUnitMaxScale"/>
    <property value="0" key="labeling/shapeOffsetMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/shapeOffsetMapUnitScale"/>
    <property value="1" key="labeling/shapeOffsetUnits"/>
    <property value="0" key="labeling/shapeOffsetX"/>
    <property value="0" key="labeling/shapeOffsetY"/>
    <property value="0" key="labeling/shapeRadiiMapUnitMaxScale"/>
    <property value="0" key="labeling/shapeRadiiMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/shapeRadiiMapUnitScale"/>
    <property value="1" key="labeling/shapeRadiiUnits"/>
    <property value="0" key="labeling/shapeRadiiX"/>
    <property value="0" key="labeling/shapeRadiiY"/>
    <property value="0" key="labeling/shapeRotation"/>
    <property value="0" key="labeling/shapeRotationType"/>
    <property value="" key="labeling/shapeSVGFile"/>
    <property value="0" key="labeling/shapeSizeMapUnitMaxScale"/>
    <property value="0" key="labeling/shapeSizeMapUnitMinScale"/>
    <property value="0,0,0,0,0,0" key="labeling/shapeSizeMapUnitScale"/>
    <property value="0" key="labeling/shapeSizeType"/>
    <property value="1" key="labeling/shapeSizeUnits"/>
    <property value="0" key="labeling/shapeSizeX"/>
    <property value="0" key="labeling/shapeSizeY"/>
    <property value="0" key="labeling/shapeTransparency"/>
    <property value="0" key="labeling/shapeType"/>
    <property value="255" key="labeling/textColorA"/>
    <property value="0" key="labeling/textColorB"/>
    <property value="0" key="labeling/textColorG"/>
    <property value="0" key="labeling/textColorR"/>
    <property value="0" key="labeling/textTransp"/>
    <property value="0" key="labeling/upsidedownLabels"/>
    <property value="" key="labeling/wrapChar"/>
    <property value="0" key="labeling/xOffset"/>
    <property value="0" key="labeling/yOffset"/>
    <property value="-1" key="labeling/zIndex"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Pie">
    <DiagramCategory backgroundColor="#ffffff" sizeScale="3x:0,0,0,0,0,0" enabled="0" sizeType="MM" maxScaleDenominator="1e+08" scaleBasedVisibility="0" opacity="1" scaleDependency="Area" width="15" lineSizeType="MM" penColor="#000000" lineSizeScale="3x:0,0,0,0,0,0" barWidth="5" penAlpha="255" height="15" diagramOrientation="Up" backgroundAlpha="255" minScaleDenominator="100000" labelPlacementMethod="XHeight" minimumSize="0" penWidth="0" rotationOffset="270">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="2" linePlacementFlags="2" obstacle="0" zIndex="0" dist="0" priority="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties" type="Map">
          <Option name="show" type="Map">
            <Option value="true" name="active" type="bool"/>
            <Option value="Y_I" name="field" type="QString"/>
            <Option value="2" name="type" type="int"/>
          </Option>
        </Option>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="L">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="X_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Y_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="X_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Y_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_COL">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_TRM_(N)">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_POS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PAV_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PAV_2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PROF_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PROF_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX01">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX02">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX03">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_X">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_Y">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_VIS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_col_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_col_p1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_tap_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_tap_p1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="S">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="DN">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Mat_col">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Caida_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Caida_p2_h">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="n">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Qt_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Qt_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Q_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Q_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yn_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yn_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yrel_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yrel_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Trativa_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Trativa_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="V_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="V_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Vc">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option value="0" name="IsMultiline" type="QString"/>
            <Option value="0" name="UseHtml" type="QString"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" field="L" index="0"/>
    <alias name="" field="X_I" index="1"/>
    <alias name="" field="Y_I" index="2"/>
    <alias name="" field="X_F" index="3"/>
    <alias name="" field="Y_F" index="4"/>
    <alias name="" field="ID_COL" index="5"/>
    <alias name="" field="ID_TRM_(N)" index="6"/>
    <alias name="" field="AUX_POS" index="7"/>
    <alias name="" field="AUX_PAV_1" index="8"/>
    <alias name="" field="AUX_PAV_2" index="9"/>
    <alias name="" field="AUX_PROF_I" index="10"/>
    <alias name="" field="AUX_PROF_F" index="11"/>
    <alias name="" field="AUX01" index="12"/>
    <alias name="" field="AUX02" index="13"/>
    <alias name="" field="AUX03" index="14"/>
    <alias name="" field="LABEL_X" index="15"/>
    <alias name="" field="LABEL_Y" index="16"/>
    <alias name="" field="LABEL_VIS" index="17"/>
    <alias name="" field="h_col_p2" index="18"/>
    <alias name="" field="h_col_p1" index="19"/>
    <alias name="" field="h_tap_p2" index="20"/>
    <alias name="" field="h_tap_p1" index="21"/>
    <alias name="" field="S" index="22"/>
    <alias name="" field="DN" index="23"/>
    <alias name="" field="Mat_col" index="24"/>
    <alias name="" field="Caida_p2" index="25"/>
    <alias name="" field="Caida_p2_h" index="26"/>
    <alias name="" field="n" index="27"/>
    <alias name="" field="Qt_i" index="28"/>
    <alias name="" field="Qt_f" index="29"/>
    <alias name="" field="Q_i" index="30"/>
    <alias name="" field="Q_f" index="31"/>
    <alias name="" field="yn_i" index="32"/>
    <alias name="" field="yn_f" index="33"/>
    <alias name="" field="yrel_i" index="34"/>
    <alias name="" field="yrel_f" index="35"/>
    <alias name="" field="Trativa_i" index="36"/>
    <alias name="" field="Trativa_f" index="37"/>
    <alias name="" field="V_i" index="38"/>
    <alias name="" field="V_f" index="39"/>
    <alias name="" field="Vc" index="40"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="L" expression=""/>
    <default applyOnUpdate="0" field="X_I" expression=""/>
    <default applyOnUpdate="0" field="Y_I" expression=""/>
    <default applyOnUpdate="0" field="X_F" expression=""/>
    <default applyOnUpdate="0" field="Y_F" expression=""/>
    <default applyOnUpdate="0" field="ID_COL" expression=""/>
    <default applyOnUpdate="0" field="ID_TRM_(N)" expression=""/>
    <default applyOnUpdate="0" field="AUX_POS" expression=""/>
    <default applyOnUpdate="0" field="AUX_PAV_1" expression=""/>
    <default applyOnUpdate="0" field="AUX_PAV_2" expression=""/>
    <default applyOnUpdate="0" field="AUX_PROF_I" expression=""/>
    <default applyOnUpdate="0" field="AUX_PROF_F" expression=""/>
    <default applyOnUpdate="0" field="AUX01" expression=""/>
    <default applyOnUpdate="0" field="AUX02" expression=""/>
    <default applyOnUpdate="0" field="AUX03" expression=""/>
    <default applyOnUpdate="0" field="LABEL_X" expression=""/>
    <default applyOnUpdate="0" field="LABEL_Y" expression=""/>
    <default applyOnUpdate="0" field="LABEL_VIS" expression=""/>
    <default applyOnUpdate="0" field="h_col_p2" expression=""/>
    <default applyOnUpdate="0" field="h_col_p1" expression=""/>
    <default applyOnUpdate="0" field="h_tap_p2" expression=""/>
    <default applyOnUpdate="0" field="h_tap_p1" expression=""/>
    <default applyOnUpdate="0" field="S" expression=""/>
    <default applyOnUpdate="0" field="DN" expression=""/>
    <default applyOnUpdate="0" field="Mat_col" expression=""/>
    <default applyOnUpdate="0" field="Caida_p2" expression=""/>
    <default applyOnUpdate="0" field="Caida_p2_h" expression=""/>
    <default applyOnUpdate="0" field="n" expression=""/>
    <default applyOnUpdate="0" field="Qt_i" expression=""/>
    <default applyOnUpdate="0" field="Qt_f" expression=""/>
    <default applyOnUpdate="0" field="Q_i" expression=""/>
    <default applyOnUpdate="0" field="Q_f" expression=""/>
    <default applyOnUpdate="0" field="yn_i" expression=""/>
    <default applyOnUpdate="0" field="yn_f" expression=""/>
    <default applyOnUpdate="0" field="yrel_i" expression=""/>
    <default applyOnUpdate="0" field="yrel_f" expression=""/>
    <default applyOnUpdate="0" field="Trativa_i" expression=""/>
    <default applyOnUpdate="0" field="Trativa_f" expression=""/>
    <default applyOnUpdate="0" field="V_i" expression=""/>
    <default applyOnUpdate="0" field="V_f" expression=""/>
    <default applyOnUpdate="0" field="Vc" expression=""/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" field="L" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="X_I" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Y_I" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="X_F" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Y_F" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="ID_COL" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="ID_TRM_(N)" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX_POS" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX_PAV_1" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX_PAV_2" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX_PROF_I" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX_PROF_F" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX01" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX02" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="AUX03" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="LABEL_X" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="LABEL_Y" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="LABEL_VIS" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="h_col_p2" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="h_col_p1" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="h_tap_p2" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="h_tap_p1" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="S" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="DN" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Mat_col" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Caida_p2" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Caida_p2_h" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="n" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Qt_i" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Qt_f" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Q_i" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Q_f" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="yn_i" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="yn_f" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="yrel_i" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="yrel_f" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Trativa_i" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Trativa_f" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="V_i" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="V_f" exp_strength="0" unique_strength="0" constraints="0"/>
    <constraint notnull_strength="0" field="Vc" exp_strength="0" unique_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="L" desc=""/>
    <constraint exp="" field="X_I" desc=""/>
    <constraint exp="" field="Y_I" desc=""/>
    <constraint exp="" field="X_F" desc=""/>
    <constraint exp="" field="Y_F" desc=""/>
    <constraint exp="" field="ID_COL" desc=""/>
    <constraint exp="" field="ID_TRM_(N)" desc=""/>
    <constraint exp="" field="AUX_POS" desc=""/>
    <constraint exp="" field="AUX_PAV_1" desc=""/>
    <constraint exp="" field="AUX_PAV_2" desc=""/>
    <constraint exp="" field="AUX_PROF_I" desc=""/>
    <constraint exp="" field="AUX_PROF_F" desc=""/>
    <constraint exp="" field="AUX01" desc=""/>
    <constraint exp="" field="AUX02" desc=""/>
    <constraint exp="" field="AUX03" desc=""/>
    <constraint exp="" field="LABEL_X" desc=""/>
    <constraint exp="" field="LABEL_Y" desc=""/>
    <constraint exp="" field="LABEL_VIS" desc=""/>
    <constraint exp="" field="h_col_p2" desc=""/>
    <constraint exp="" field="h_col_p1" desc=""/>
    <constraint exp="" field="h_tap_p2" desc=""/>
    <constraint exp="" field="h_tap_p1" desc=""/>
    <constraint exp="" field="S" desc=""/>
    <constraint exp="" field="DN" desc=""/>
    <constraint exp="" field="Mat_col" desc=""/>
    <constraint exp="" field="Caida_p2" desc=""/>
    <constraint exp="" field="Caida_p2_h" desc=""/>
    <constraint exp="" field="n" desc=""/>
    <constraint exp="" field="Qt_i" desc=""/>
    <constraint exp="" field="Qt_f" desc=""/>
    <constraint exp="" field="Q_i" desc=""/>
    <constraint exp="" field="Q_f" desc=""/>
    <constraint exp="" field="yn_i" desc=""/>
    <constraint exp="" field="yn_f" desc=""/>
    <constraint exp="" field="yrel_i" desc=""/>
    <constraint exp="" field="yrel_f" desc=""/>
    <constraint exp="" field="Trativa_i" desc=""/>
    <constraint exp="" field="Trativa_f" desc=""/>
    <constraint exp="" field="V_i" desc=""/>
    <constraint exp="" field="V_f" desc=""/>
    <constraint exp="" field="Vc" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
    <actionsetting id="{e3f1e32a-cc2e-4374-a361-cfba4a304376}" shortTitle="" action="echo &quot;[% &quot;MY_FIELD&quot; %]&quot;" name="Eco do valor de atributo" isEnabledOnlyWhenEditable="0" icon="" capture="1" type="0" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
    <actionsetting id="{53090f62-d041-4171-83c7-16c9f01efb96}" shortTitle="" action="ogr2ogr -f &quot;ESRI Shapefile&quot; &quot;[% &quot;OUTPUT_PATH&quot; %]&quot; &quot;[% &quot;INPUT_FILE&quot; %]&quot;" name="Rodar aplicação" isEnabledOnlyWhenEditable="0" icon="" capture="1" type="0" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
    <actionsetting id="{a6e8eda2-edfb-4139-a654-7e294195ef25}" shortTitle="" action="QtGui.QMessageBox.information(None, &quot;Feature id&quot;, &quot;feature id is [% $id %]&quot;)" name="Obter feição id" isEnabledOnlyWhenEditable="0" icon="" capture="0" type="1" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
    <actionsetting id="{99ab3d44-0675-4c24-82de-c521df7ba996}" shortTitle="" action="QtGui.QMessageBox.information(None, &quot;Current field's value&quot;, &quot;[% $currentfield %]&quot;)" name="Selecionar valores de campo (Identificar ferramentas de identificação)" isEnabledOnlyWhenEditable="0" icon="" capture="0" type="1" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
    <actionsetting id="{4d39d538-9c29-46bf-8dea-a04f3fc5343b}" shortTitle="" action="QtGui.QMessageBox.information(None, &quot;Clicked coords&quot;, &quot;layer: [% $layerid %]\ncoords: ([% $clickx %],[% $clicky %])&quot;)" name="Coordenadas clicadas (Rodar ferramentas de ações de feições)" isEnabledOnlyWhenEditable="0" icon="" capture="0" type="1" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
    <actionsetting id="{2b619b9b-59e1-4af3-bb48-e1ee04439aab}" shortTitle="" action="[% &quot;PATH&quot; %]" name="Abrir arquivo" isEnabledOnlyWhenEditable="0" icon="" capture="0" type="5" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
    <actionsetting id="{df957b35-263b-44de-9fab-ff8ef523e225}" shortTitle="" action="http://www.google.com/search?q=[% &quot;ATTRIBUTE&quot; %]" name="Buscar na web valores de atributo" isEnabledOnlyWhenEditable="0" icon="" capture="0" type="5" notificationMessage="">
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
      <actionScope id="Field"/>
    </actionsetting>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column width="-1" name="Y_I" type="field" hidden="0"/>
      <column width="-1" name="AUX_PAV_2" type="field" hidden="0"/>
      <column width="-1" name="AUX_PAV_1" type="field" hidden="0"/>
      <column width="-1" name="X_I" type="field" hidden="0"/>
      <column width="-1" name="AUX03" type="field" hidden="0"/>
      <column width="-1" name="AUX02" type="field" hidden="0"/>
      <column width="-1" name="AUX01" type="field" hidden="0"/>
      <column width="-1" name="AUX_PROF_I" type="field" hidden="0"/>
      <column width="-1" name="ID_COL" type="field" hidden="0"/>
      <column width="-1" name="AUX_POS" type="field" hidden="0"/>
      <column width="-1" name="LABEL_VIS" type="field" hidden="0"/>
      <column width="-1" name="ID_TRM_(N)" type="field" hidden="0"/>
      <column width="-1" name="L" type="field" hidden="0"/>
      <column width="-1" name="AUX_PROF_F" type="field" hidden="0"/>
      <column width="-1" name="X_F" type="field" hidden="0"/>
      <column width="-1" name="Y_F" type="field" hidden="0"/>
      <column width="-1" name="LABEL_X" type="field" hidden="0"/>
      <column width="-1" name="LABEL_Y" type="field" hidden="0"/>
      <column width="-1" name="h_col_p2" type="field" hidden="0"/>
      <column width="-1" name="h_col_p1" type="field" hidden="0"/>
      <column width="-1" name="S" type="field" hidden="0"/>
      <column width="-1" name="DN" type="field" hidden="0"/>
      <column width="-1" name="Mat_col" type="field" hidden="0"/>
      <column width="-1" name="Caida_p2" type="field" hidden="0"/>
      <column width="-1" name="Caida_p2_h" type="field" hidden="0"/>
      <column width="-1" name="n" type="field" hidden="0"/>
      <column width="-1" name="Qt_i" type="field" hidden="0"/>
      <column width="-1" name="Qt_f" type="field" hidden="0"/>
      <column width="-1" name="Q_i" type="field" hidden="0"/>
      <column width="-1" name="Q_f" type="field" hidden="0"/>
      <column width="-1" name="yn_i" type="field" hidden="0"/>
      <column width="-1" name="yn_f" type="field" hidden="0"/>
      <column width="-1" name="yrel_i" type="field" hidden="0"/>
      <column width="-1" name="yrel_f" type="field" hidden="0"/>
      <column width="-1" name="Trativa_i" type="field" hidden="0"/>
      <column width="-1" name="Trativa_f" type="field" hidden="0"/>
      <column width="-1" name="V_i" type="field" hidden="0"/>
      <column width="-1" name="V_f" type="field" hidden="0"/>
      <column width="-1" name="Vc" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" name="h_tap_p2" type="field" hidden="0"/>
      <column width="-1" name="h_tap_p1" type="field" hidden="0"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1">.</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>.</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- codificação: utf-8 -*-
"""
Os formulários do QGIS podem ter uma função Python que é chamada quando
o formulário
 é aberto.

QGIS forms can have a Python function that is called when the form is
opened.

Use esta função para adicionar lógica extra aos seus formulários.

Entre com o nome da função no campo "Python Init function".
Un exemplo a seguir:
"""
a partir de PyQt4.QtGui importe QWidget

def my_form_open(diálogo, camada, feição):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>1</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="AUX01" editable="1"/>
    <field name="AUX02" editable="1"/>
    <field name="AUX03" editable="1"/>
    <field name="AUX_PAV_1" editable="1"/>
    <field name="AUX_PAV_2" editable="1"/>
    <field name="AUX_POS" editable="1"/>
    <field name="AUX_PROF_F" editable="1"/>
    <field name="AUX_PROF_I" editable="1"/>
    <field name="Caida_p2" editable="1"/>
    <field name="Caida_p2_h" editable="1"/>
    <field name="DN" editable="1"/>
    <field name="ID_COL" editable="1"/>
    <field name="ID_TRM_(N)" editable="1"/>
    <field name="L" editable="1"/>
    <field name="LABEL_VIS" editable="1"/>
    <field name="LABEL_X" editable="1"/>
    <field name="LABEL_Y" editable="1"/>
    <field name="Mat_col" editable="1"/>
    <field name="Q_f" editable="1"/>
    <field name="Q_i" editable="1"/>
    <field name="Qt_f" editable="1"/>
    <field name="Qt_i" editable="1"/>
    <field name="S" editable="1"/>
    <field name="Trativa_f" editable="1"/>
    <field name="Trativa_i" editable="1"/>
    <field name="V_f" editable="1"/>
    <field name="V_i" editable="1"/>
    <field name="Vc" editable="1"/>
    <field name="X_F" editable="1"/>
    <field name="X_I" editable="1"/>
    <field name="Y_F" editable="1"/>
    <field name="Y_I" editable="1"/>
    <field name="h_col_p1" editable="1"/>
    <field name="h_col_p2" editable="1"/>
    <field name="h_tap_p1" editable="1"/>
    <field name="h_tap_p2" editable="1"/>
    <field name="n" editable="1"/>
    <field name="yn_f" editable="1"/>
    <field name="yn_i" editable="1"/>
    <field name="yrel_f" editable="1"/>
    <field name="yrel_i" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="AUX01" labelOnTop="0"/>
    <field name="AUX02" labelOnTop="0"/>
    <field name="AUX03" labelOnTop="0"/>
    <field name="AUX_PAV_1" labelOnTop="0"/>
    <field name="AUX_PAV_2" labelOnTop="0"/>
    <field name="AUX_POS" labelOnTop="0"/>
    <field name="AUX_PROF_F" labelOnTop="0"/>
    <field name="AUX_PROF_I" labelOnTop="0"/>
    <field name="Caida_p2" labelOnTop="0"/>
    <field name="Caida_p2_h" labelOnTop="0"/>
    <field name="DN" labelOnTop="0"/>
    <field name="ID_COL" labelOnTop="0"/>
    <field name="ID_TRM_(N)" labelOnTop="0"/>
    <field name="L" labelOnTop="0"/>
    <field name="LABEL_VIS" labelOnTop="0"/>
    <field name="LABEL_X" labelOnTop="0"/>
    <field name="LABEL_Y" labelOnTop="0"/>
    <field name="Mat_col" labelOnTop="0"/>
    <field name="Q_f" labelOnTop="0"/>
    <field name="Q_i" labelOnTop="0"/>
    <field name="Qt_f" labelOnTop="0"/>
    <field name="Qt_i" labelOnTop="0"/>
    <field name="S" labelOnTop="0"/>
    <field name="Trativa_f" labelOnTop="0"/>
    <field name="Trativa_i" labelOnTop="0"/>
    <field name="V_f" labelOnTop="0"/>
    <field name="V_i" labelOnTop="0"/>
    <field name="Vc" labelOnTop="0"/>
    <field name="X_F" labelOnTop="0"/>
    <field name="X_I" labelOnTop="0"/>
    <field name="Y_F" labelOnTop="0"/>
    <field name="Y_I" labelOnTop="0"/>
    <field name="h_col_p1" labelOnTop="0"/>
    <field name="h_col_p2" labelOnTop="0"/>
    <field name="h_tap_p1" labelOnTop="0"/>
    <field name="h_tap_p2" labelOnTop="0"/>
    <field name="n" labelOnTop="0"/>
    <field name="yn_f" labelOnTop="0"/>
    <field name="yn_i" labelOnTop="0"/>
    <field name="yrel_f" labelOnTop="0"/>
    <field name="yrel_i" labelOnTop="0"/>
  </labelOnTop>
  <widgets>
    <widget name="123_COTAF">
      <config/>
    </widget>
    <widget name="123_COTAT">
      <config/>
    </widget>
    <widget name="123_DECLIVIDADE">
      <config/>
    </widget>
    <widget name="123_DIAM">
      <config/>
    </widget>
    <widget name="123_NO_ESTRU">
      <config/>
    </widget>
    <widget name="123_PROF2">
      <config/>
    </widget>
    <widget name="123_PROFPV">
      <config/>
    </widget>
    <widget name="123_QE">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_COTAF">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_COTAT">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_DECLIVIDADE">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_DIAM">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_NO_ESTRU">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_PROF2">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_PROFPV">
      <config/>
    </widget>
    <widget name="Atributos Hoja Calculo_QE">
      <config/>
    </widget>
  </widgets>
  <previewExpression>ID_COL</previewExpression>
  <mapTip>ID</mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
