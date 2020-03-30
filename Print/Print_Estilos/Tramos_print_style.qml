<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="1" simplifyDrawingTol="1" styleCategories="AllStyleCategories" readOnly="0" simplifyDrawingHints="1" minScale="1e+08" version="3.4.2-Madeira" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" maxScale="100000" simplifyLocal="1" simplifyAlgorithm="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" type="RuleRenderer" symbollevels="0" enableorderby="0">
    <rules key="{7b6772ff-b392-462e-910b-bc97815c9341}">
      <rule symbol="0" key="{89fa5778-836a-4f4c-8b63-e9f38d289fe2}" filter=" &quot;L&quot; &lt;> 0"/>
      <rule symbol="1" key="{97cbed74-e7cf-4194-8afd-bb33570d294a}" filter=" &quot;Caida_p2&quot; ='D'"/>
      <rule symbol="2" key="{a324e7fc-3afb-48c8-86ba-ac3b5a893d55}" filter=" &quot;Caida_p2_h&quot;   > 0 and   &quot;Caida_p2&quot;   = 'TC'"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" name="0" alpha="1" type="line">
        <layer enabled="1" locked="0" class="SimpleLine" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MapUnit" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="4,0,241,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.4" k="line_width"/>
          <prop v="MapUnit" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer enabled="1" locked="0" class="MarkerLine" pass="1">
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MapUnit" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MapUnit" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="vertex" k="placement"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@0@1" alpha="1" type="marker">
            <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
              <prop v="0" k="angle"/>
              <prop v="0,0,0,0" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MapUnit" k="offset_unit"/>
              <prop v="170,0,0,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0.5" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MapUnit" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="6" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MapUnit" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer enabled="1" locked="0" class="MarkerLine" pass="2">
          <prop v="3" k="interval"/>
          <prop v="3x:0,0,0,0,0,0" k="interval_map_unit_scale"/>
          <prop v="MapUnit" k="interval_unit"/>
          <prop v="0" k="offset"/>
          <prop v="0" k="offset_along_line"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_along_line_map_unit_scale"/>
          <prop v="MapUnit" k="offset_along_line_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MapUnit" k="offset_unit"/>
          <prop v="centralpoint" k="placement"/>
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@0@2" alpha="1" type="marker">
            <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
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
              <prop v="1.1" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MapUnit" k="outline_width_unit"/>
              <prop v="area" k="scale_method"/>
              <prop v="5" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MapUnit" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties" type="Map">
                    <Option name="name" type="Map">
                      <Option name="active" type="bool" value="false"/>
                      <Option name="field" type="QString" value="COTAF"/>
                      <Option name="type" type="int" value="2"/>
                    </Option>
                  </Option>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="1" alpha="1" type="line">
        <layer enabled="1" locked="0" class="MarkerLine" pass="0">
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
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@1@0" alpha="1" type="marker">
            <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" name="2" alpha="1" type="line">
        <layer enabled="1" locked="0" class="MarkerLine" pass="0">
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
          <prop v="1" k="rotate"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@2@0" alpha="1" type="marker">
            <layer enabled="1" locked="0" class="SimpleMarker" pass="0">
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
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{2842072d-8e31-4d3f-8811-f2c26c5e2ddd}">
      <rule key="{735ce2cc-1cc7-4f95-bdfe-92b750838e59}" filter=" &quot;Caida_p2_h&quot;  &lt;= 0.03999 or  &quot;Caida_p2_h&quot;  is NULL">
        <settings>
          <text-style fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" blendMode="0" fontUnderline="0" fieldName="   &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xa;     ''  || '\n' ||&#xa;     'Ø' ||   &quot;DN&quot;    || '\n' || &#xa;        &quot;S&quot;  " fontCapitals="0" fontLetterSpacing="0" fontWeight="50" fontSizeUnit="MapUnit" isExpression="1" fontItalic="0" namedStyle="Normal" textOpacity="1" fontWordSpacing="0" fontFamily="Arial" useSubstitutions="0" fontSize="3.6" textColor="0,0,0,255" previewBkgrdColor="#ffffff" multilineHeight="1">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferSize="0.7" bufferBlendMode="0" bufferJoinStyle="64" bufferSizeUnits="MapUnit" bufferOpacity="0.4" bufferColor="255,255,255,255" bufferNoFill="0"/>
            <background shapeRadiiY="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeDraw="0" shapeSVGFile="" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeRotationType="0" shapeOffsetY="0" shapeOpacity="1" shapeRadiiX="0" shapeType="0" shapeSizeUnit="MM" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeJoinStyle="64" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0"/>
            <shadow shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5" shadowScale="100" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format addDirectionSymbol="0" formatNumbers="0" autoWrapLength="0" plussign="0" decimals="3" reverseDirectionSymbol="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" wrapChar="" useMaxLineLengthForAutoWrap="1" multilineAlign="1" rightDirectionSymbol=">"/>
          <placement rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" offsetType="0" centroidInside="0" placement="2" yOffset="0" maxCurvedCharAngleOut="-20" priority="5" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="20" preserveRotation="1" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" quadOffset="4" xOffset="0" distUnits="MM" offsetUnits="MapUnit" dist="0" centroidWhole="0"/>
          <rendering labelPerPart="0" scaleMax="2001" fontLimitPixelSize="0" maxNumLabels="2000" obstacle="0" scaleMin="1" obstacleFactor="1" obstacleType="0" drawLabels="1" displayAll="1" mergeLines="0" minFeatureSize="0" scaleVisibility="1" fontMaxPixelSize="10000" upsidedownLabels="0" fontMinPixelSize="3" limitNumLabels="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_X"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_Y"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
                <Option name="Show" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_VIS"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
              </Option>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{106d5ca7-6ca4-4f52-b1f8-c8be74a0a7b6}" filter=" &quot;Caida_p2_h&quot;  &lt;>0 and &quot;Caida_p2&quot;  ='TC'">
        <settings>
          <text-style fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" blendMode="0" fontUnderline="0" fieldName="    &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xd;&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xd;&#xa;     ''  || '\n' ||&#xd;&#xa;&#x9;  ''  || '\n' ||&#xd;&#xa;      'Ø' ||   &quot;DN&quot;    || '\n' || &#xd;&#xa;        &quot;S&quot;  || '\n' || &#xd;&#xa;&#x9;&#x9; &quot;Caida_p2&quot;   || ' '||   &quot;Caida_p2_h&quot;" fontCapitals="0" fontLetterSpacing="0" fontWeight="50" fontSizeUnit="MapUnit" isExpression="1" fontItalic="0" namedStyle="Normal" textOpacity="1" fontWordSpacing="0" fontFamily="Arial" useSubstitutions="0" fontSize="3.6" textColor="0,0,0,255" previewBkgrdColor="#ffffff" multilineHeight="0.92">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferSize="0.7" bufferBlendMode="0" bufferJoinStyle="64" bufferSizeUnits="MapUnit" bufferOpacity="0.4" bufferColor="255,255,255,255" bufferNoFill="0"/>
            <background shapeRadiiY="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeDraw="0" shapeSVGFile="" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeRotationType="0" shapeOffsetY="0" shapeOpacity="1" shapeRadiiX="0" shapeType="0" shapeSizeUnit="MM" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeJoinStyle="64" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0"/>
            <shadow shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5" shadowScale="100" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format addDirectionSymbol="0" formatNumbers="0" autoWrapLength="0" plussign="0" decimals="3" reverseDirectionSymbol="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" wrapChar="" useMaxLineLengthForAutoWrap="1" multilineAlign="1" rightDirectionSymbol=">"/>
          <placement rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" offsetType="0" centroidInside="0" placement="2" yOffset="0" maxCurvedCharAngleOut="-20" priority="5" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="20" preserveRotation="1" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" quadOffset="4" xOffset="0" distUnits="MM" offsetUnits="MapUnit" dist="0" centroidWhole="0"/>
          <rendering labelPerPart="0" scaleMax="2001" fontLimitPixelSize="0" maxNumLabels="2000" obstacle="0" scaleMin="1" obstacleFactor="1" obstacleType="0" drawLabels="1" displayAll="1" mergeLines="0" minFeatureSize="0" scaleVisibility="1" fontMaxPixelSize="10000" upsidedownLabels="0" fontMinPixelSize="3" limitNumLabels="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_X"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_Y"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
                <Option name="Show" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_VIS"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
              </Option>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{3ed874c8-fc01-4270-bdc7-ebd140b1113d}" filter=" &quot;Caida_p2_h&quot;  > 0.0399 and &quot;Caida_p2&quot; ='D'">
        <settings>
          <text-style fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" blendMode="0" fontUnderline="0" fieldName="    &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xd;&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xd;&#xa;     ''  || '\n' ||&#xd;&#xa;&#x9;  ''  || '\n' ||&#xd;&#xa;      'Ø' ||   &quot;DN&quot;    || '\n' || &#xd;&#xa;        &quot;S&quot;  || '\n' || &#xd;&#xa;&#x9;&#x9;  'D'   || ' '||  &quot;Caida_p2_h&quot;" fontCapitals="0" fontLetterSpacing="0" fontWeight="50" fontSizeUnit="MapUnit" isExpression="1" fontItalic="0" namedStyle="Normal" textOpacity="1" fontWordSpacing="0" fontFamily="Arial" useSubstitutions="0" fontSize="3.6" textColor="0,0,0,255" previewBkgrdColor="#ffffff" multilineHeight="0.92">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferSize="0.7" bufferBlendMode="0" bufferJoinStyle="64" bufferSizeUnits="MapUnit" bufferOpacity="0.4" bufferColor="255,255,255,255" bufferNoFill="0"/>
            <background shapeRadiiY="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeDraw="0" shapeSVGFile="" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeRotationType="0" shapeOffsetY="0" shapeOpacity="1" shapeRadiiX="0" shapeType="0" shapeSizeUnit="MM" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeJoinStyle="64" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0"/>
            <shadow shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5" shadowScale="100" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format addDirectionSymbol="0" formatNumbers="0" autoWrapLength="0" plussign="0" decimals="3" reverseDirectionSymbol="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" wrapChar="" useMaxLineLengthForAutoWrap="1" multilineAlign="1" rightDirectionSymbol=">"/>
          <placement rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" offsetType="0" centroidInside="0" placement="2" yOffset="0" maxCurvedCharAngleOut="-20" priority="5" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="20" preserveRotation="1" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" quadOffset="4" xOffset="0" distUnits="MM" offsetUnits="MapUnit" dist="0" centroidWhole="0"/>
          <rendering labelPerPart="0" scaleMax="2001" fontLimitPixelSize="0" maxNumLabels="2000" obstacle="0" scaleMin="1" obstacleFactor="1" obstacleType="0" drawLabels="1" displayAll="1" mergeLines="0" minFeatureSize="0" scaleVisibility="1" fontMaxPixelSize="10000" upsidedownLabels="0" fontMinPixelSize="3" limitNumLabels="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties" type="Map">
                <Option name="PositionX" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_X"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
                <Option name="PositionY" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="Y_F"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
                <Option name="Show" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_VIS"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
              </Option>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{cdf2ef02-6d7c-426f-8c2e-c0fe72d30c18}">
        <settings>
          <text-style fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" blendMode="0" fontUnderline="0" fieldName="ID_TRM_(N)" fontCapitals="0" fontLetterSpacing="0" fontWeight="50" fontSizeUnit="Point" isExpression="0" fontItalic="0" namedStyle="Normal" textOpacity="1" fontWordSpacing="0" fontFamily="Arial" useSubstitutions="0" fontSize="8.25" textColor="0,0,0,255" previewBkgrdColor="#ffffff" multilineHeight="1">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferSize="0.7" bufferBlendMode="0" bufferJoinStyle="64" bufferSizeUnits="MapUnit" bufferOpacity="0.4" bufferColor="255,255,255,255" bufferNoFill="0"/>
            <background shapeRadiiY="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeDraw="0" shapeSVGFile="" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeRotationType="0" shapeOffsetY="0" shapeOpacity="1" shapeRadiiX="0" shapeType="0" shapeSizeUnit="MM" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeJoinStyle="64" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0"/>
            <shadow shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5" shadowScale="100" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format addDirectionSymbol="0" formatNumbers="0" autoWrapLength="0" plussign="0" decimals="3" reverseDirectionSymbol="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" wrapChar="" useMaxLineLengthForAutoWrap="1" multilineAlign="1" rightDirectionSymbol=">"/>
          <placement rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" offsetType="0" centroidInside="0" placement="2" yOffset="0" maxCurvedCharAngleOut="-20" priority="5" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="20" preserveRotation="1" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="10" quadOffset="4" xOffset="0" distUnits="MM" offsetUnits="MapUnit" dist="0" centroidWhole="0"/>
          <rendering labelPerPart="0" scaleMax="6000" fontLimitPixelSize="0" maxNumLabels="2000" obstacle="0" scaleMin="2002" obstacleFactor="1" obstacleType="0" drawLabels="1" displayAll="0" mergeLines="0" minFeatureSize="0" scaleVisibility="1" fontMaxPixelSize="10000" upsidedownLabels="0" fontMinPixelSize="3" limitNumLabels="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties" type="Map">
                <Option name="Show" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_VIS"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
              </Option>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{fe14165c-c3a1-4b3c-af6f-b5934cc46679}">
        <settings>
          <text-style fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" blendMode="0" fontUnderline="0" fieldName="'col'  || ID_COL" fontCapitals="0" fontLetterSpacing="0" fontWeight="50" fontSizeUnit="Point" isExpression="1" fontItalic="0" namedStyle="Normal" textOpacity="1" fontWordSpacing="0" fontFamily="Arial" useSubstitutions="0" fontSize="8.25" textColor="0,0,0,255" previewBkgrdColor="#ffffff" multilineHeight="1">
            <text-buffer bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferDraw="1" bufferSize="0.7" bufferBlendMode="0" bufferJoinStyle="64" bufferSizeUnits="MapUnit" bufferOpacity="0.4" bufferColor="255,255,255,255" bufferNoFill="0"/>
            <background shapeRadiiY="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeRadiiUnit="MM" shapeDraw="0" shapeSVGFile="" shapeOffsetX="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeRotationType="0" shapeOffsetY="0" shapeOpacity="1" shapeRadiiX="0" shapeType="0" shapeSizeUnit="MM" shapeBorderWidth="0" shapeOffsetUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeBorderColor="128,128,128,255" shapeJoinStyle="64" shapeSizeType="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0"/>
            <shadow shadowOffsetAngle="135" shadowRadiusAlphaOnly="0" shadowOpacity="0.7" shadowUnder="0" shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowDraw="0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadius="1.5" shadowScale="100" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowRadiusUnit="MM"/>
            <substitutions/>
          </text-style>
          <text-format addDirectionSymbol="0" formatNumbers="0" autoWrapLength="0" plussign="0" decimals="3" reverseDirectionSymbol="0" placeDirectionSymbol="0" leftDirectionSymbol="&lt;" wrapChar="" useMaxLineLengthForAutoWrap="1" multilineAlign="1" rightDirectionSymbol=">"/>
          <placement rotationAngle="0" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" offsetType="0" centroidInside="0" placement="2" yOffset="0" maxCurvedCharAngleOut="-20" priority="5" fitInPolygonOnly="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="20" preserveRotation="1" repeatDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="10" quadOffset="4" xOffset="0" distUnits="MM" offsetUnits="MapUnit" dist="0" centroidWhole="0"/>
          <rendering labelPerPart="0" scaleMax="10000" fontLimitPixelSize="0" maxNumLabels="2000" obstacle="0" scaleMin="6001" obstacleFactor="1" obstacleType="0" drawLabels="1" displayAll="0" mergeLines="0" minFeatureSize="0" scaleVisibility="1" fontMaxPixelSize="10000" upsidedownLabels="0" fontMinPixelSize="3" limitNumLabels="0" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties" type="Map">
                <Option name="Show" type="Map">
                  <Option name="active" type="bool" value="true"/>
                  <Option name="field" type="QString" value="LABEL_VIS"/>
                  <Option name="type" type="int" value="2"/>
                </Option>
              </Option>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="true"/>
    <property key="labeling/bufferJoinStyle" value="64"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="1"/>
    <property key="labeling/bufferSizeInMapUnits" value="true"/>
    <property key="labeling/bufferSizeMapUnitMaxScale" value="0"/>
    <property key="labeling/bufferSizeMapUnitMinScale" value="0"/>
    <property key="labeling/bufferSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/bufferTransp" value="50"/>
    <property key="labeling/centroidInside" value="false"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/decimals" value="3"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="0"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/distMapUnitMaxScale" value="0"/>
    <property key="labeling/distMapUnitMinScale" value="0"/>
    <property key="labeling/distMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/drawLabels" value="true"/>
    <property key="labeling/enabled" value="true"/>
    <property key="labeling/fieldName" value="  &quot;TRM&quot; ||  '\n'  ||&#xa;    &quot;EXT&quot;   || 'm'  ||  '\n'  ||&#xa;    ''  || '\n' || &#xa;     'Ø' ||  &quot;DIAM&quot;   || '\n' || &#xa;       &quot;DECLIVIDADE&quot;  ||  '\n'  || &#xd;&#xa;&#x9;&#x9; &quot;DISPOSIT&quot;  ||  &quot;ALTURA TQ&quot; "/>
    <property key="labeling/fitInPolygonOnly" value="false"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="MS Shell Dlg 2"/>
    <property key="labeling/fontItalic" value="false"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="8.25"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontSizeMapUnitMaxScale" value="0"/>
    <property key="labeling/fontSizeMapUnitMinScale" value="0"/>
    <property key="labeling/fontSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="50"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="true"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelOffsetMapUnitMaxScale" value="0"/>
    <property key="labeling/labelOffsetMapUnitMinScale" value="0"/>
    <property key="labeling/labelOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="20"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="1"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Normal"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/obstacleFactor" value="1"/>
    <property key="labeling/obstacleType" value="0"/>
    <property key="labeling/offsetType" value="0"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="2"/>
    <property key="labeling/placementFlags" value="9"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/predefinedPositionOrder" value="TR,TL,BR,BL,R,L,TSR,BSR"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/repeatDistance" value="0"/>
    <property key="labeling/repeatDistanceMapUnitMaxScale" value="0"/>
    <property key="labeling/repeatDistanceMapUnitMinScale" value="0"/>
    <property key="labeling/repeatDistanceMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/repeatDistanceUnit" value="1"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="4000"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="true"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetMapUnitMaxScale" value="0"/>
    <property key="labeling/shadowOffsetMapUnitMinScale" value="0"/>
    <property key="labeling/shadowOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusMapUnitMaxScale" value="0"/>
    <property key="labeling/shadowRadiusMapUnitMinScale" value="0"/>
    <property key="labeling/shadowRadiusMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitMinScale" value="0"/>
    <property key="labeling/shapeBorderWidthMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeOffsetMapUnitMinScale" value="0"/>
    <property key="labeling/shapeOffsetMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeRadiiMapUnitMinScale" value="0"/>
    <property key="labeling/shapeRadiiMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeMapUnitMaxScale" value="0"/>
    <property key="labeling/shapeSizeMapUnitMinScale" value="0"/>
    <property key="labeling/shapeSizeMapUnitScale" value="0,0,0,0,0,0"/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="0"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
    <property key="labeling/zIndex" value="-1"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Pie">
    <DiagramCategory opacity="1" width="15" penColor="#000000" diagramOrientation="Up" sizeType="MM" sizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" scaleDependency="Area" lineSizeScale="3x:0,0,0,0,0,0" minScaleDenominator="100000" penWidth="0" enabled="0" scaleBasedVisibility="0" height="15" barWidth="5" rotationOffset="270" lineSizeType="MM" maxScaleDenominator="1e+08" penAlpha="255" labelPlacementMethod="XHeight" backgroundColor="#ffffff" minimumSize="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" showAll="1" placement="2" dist="0" linePlacementFlags="2" obstacle="0" priority="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties" type="Map">
          <Option name="show" type="Map">
            <Option name="active" type="bool" value="true"/>
            <Option name="field" type="QString" value="fid"/>
            <Option name="type" type="int" value="2"/>
          </Option>
        </Option>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Y_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PAV_2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PAV_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="X_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX03">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX02">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX01">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PROF_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_COL">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_POS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_VIS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_TRM_(N)">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="L">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PROF_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="X_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Y_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_X">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_Y">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_col_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_col_p1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_tap_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_tap_p1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="S">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="DN">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Mat_col">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Caida_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Caida_p2_h">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="n">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Qt_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Qt_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Q_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Q_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yn_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yn_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yrel_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yrel_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Trativa_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Trativa_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="V_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="V_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Vc">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option name="IsMultiline" type="QString" value="0"/>
            <Option name="UseHtml" type="QString" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Id_NODO_(n">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Nodo_tipo">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="CF_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="h_nodo_NT">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="h_nodo_tp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="CItrd_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Tap_nodo">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="Y_I" index="1" name=""/>
    <alias field="AUX_PAV_2" index="2" name=""/>
    <alias field="AUX_PAV_1" index="3" name=""/>
    <alias field="X_I" index="4" name=""/>
    <alias field="AUX03" index="5" name=""/>
    <alias field="AUX02" index="6" name=""/>
    <alias field="AUX01" index="7" name=""/>
    <alias field="AUX_PROF_I" index="8" name=""/>
    <alias field="ID_COL" index="9" name=""/>
    <alias field="AUX_POS" index="10" name=""/>
    <alias field="LABEL_VIS" index="11" name=""/>
    <alias field="ID_TRM_(N)" index="12" name=""/>
    <alias field="L" index="13" name=""/>
    <alias field="AUX_PROF_F" index="14" name=""/>
    <alias field="X_F" index="15" name=""/>
    <alias field="Y_F" index="16" name=""/>
    <alias field="LABEL_X" index="17" name=""/>
    <alias field="LABEL_Y" index="18" name=""/>
    <alias field="h_col_p2" index="19" name=""/>
    <alias field="h_col_p1" index="20" name=""/>
    <alias field="h_tap_p2" index="21" name=""/>
    <alias field="h_tap_p1" index="22" name=""/>
    <alias field="S" index="23" name=""/>
    <alias field="DN" index="24" name=""/>
    <alias field="Mat_col" index="25" name=""/>
    <alias field="Caida_p2" index="26" name=""/>
    <alias field="Caida_p2_h" index="27" name=""/>
    <alias field="n" index="28" name=""/>
    <alias field="Qt_i" index="29" name=""/>
    <alias field="Qt_f" index="30" name=""/>
    <alias field="Q_i" index="31" name=""/>
    <alias field="Q_f" index="32" name=""/>
    <alias field="yn_i" index="33" name=""/>
    <alias field="yn_f" index="34" name=""/>
    <alias field="yrel_i" index="35" name=""/>
    <alias field="yrel_f" index="36" name=""/>
    <alias field="Trativa_i" index="37" name=""/>
    <alias field="Trativa_f" index="38" name=""/>
    <alias field="V_i" index="39" name=""/>
    <alias field="V_f" index="40" name=""/>
    <alias field="Vc" index="41" name=""/>
    <alias field="Id_NODO_(n" index="42" name=""/>
    <alias field="Nodo_tipo" index="43" name=""/>
    <alias field="CF_nodo" index="44" name=""/>
    <alias field="h_nodo_NT" index="45" name=""/>
    <alias field="h_nodo_tp" index="46" name=""/>
    <alias field="CItrd_nodo" index="47" name=""/>
    <alias field="Tap_nodo" index="48" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="fid" expression="" applyOnUpdate="0"/>
    <default field="Y_I" expression="" applyOnUpdate="0"/>
    <default field="AUX_PAV_2" expression="" applyOnUpdate="0"/>
    <default field="AUX_PAV_1" expression="" applyOnUpdate="0"/>
    <default field="X_I" expression="" applyOnUpdate="0"/>
    <default field="AUX03" expression="" applyOnUpdate="0"/>
    <default field="AUX02" expression="" applyOnUpdate="0"/>
    <default field="AUX01" expression="" applyOnUpdate="0"/>
    <default field="AUX_PROF_I" expression="" applyOnUpdate="0"/>
    <default field="ID_COL" expression="" applyOnUpdate="0"/>
    <default field="AUX_POS" expression="" applyOnUpdate="0"/>
    <default field="LABEL_VIS" expression="" applyOnUpdate="0"/>
    <default field="ID_TRM_(N)" expression="" applyOnUpdate="0"/>
    <default field="L" expression="" applyOnUpdate="0"/>
    <default field="AUX_PROF_F" expression="" applyOnUpdate="0"/>
    <default field="X_F" expression="" applyOnUpdate="0"/>
    <default field="Y_F" expression="" applyOnUpdate="0"/>
    <default field="LABEL_X" expression="" applyOnUpdate="0"/>
    <default field="LABEL_Y" expression="" applyOnUpdate="0"/>
    <default field="h_col_p2" expression="" applyOnUpdate="0"/>
    <default field="h_col_p1" expression="" applyOnUpdate="0"/>
    <default field="h_tap_p2" expression="" applyOnUpdate="0"/>
    <default field="h_tap_p1" expression="" applyOnUpdate="0"/>
    <default field="S" expression="" applyOnUpdate="0"/>
    <default field="DN" expression="" applyOnUpdate="0"/>
    <default field="Mat_col" expression="" applyOnUpdate="0"/>
    <default field="Caida_p2" expression="" applyOnUpdate="0"/>
    <default field="Caida_p2_h" expression="" applyOnUpdate="0"/>
    <default field="n" expression="" applyOnUpdate="0"/>
    <default field="Qt_i" expression="" applyOnUpdate="0"/>
    <default field="Qt_f" expression="" applyOnUpdate="0"/>
    <default field="Q_i" expression="" applyOnUpdate="0"/>
    <default field="Q_f" expression="" applyOnUpdate="0"/>
    <default field="yn_i" expression="" applyOnUpdate="0"/>
    <default field="yn_f" expression="" applyOnUpdate="0"/>
    <default field="yrel_i" expression="" applyOnUpdate="0"/>
    <default field="yrel_f" expression="" applyOnUpdate="0"/>
    <default field="Trativa_i" expression="" applyOnUpdate="0"/>
    <default field="Trativa_f" expression="" applyOnUpdate="0"/>
    <default field="V_i" expression="" applyOnUpdate="0"/>
    <default field="V_f" expression="" applyOnUpdate="0"/>
    <default field="Vc" expression="" applyOnUpdate="0"/>
    <default field="Id_NODO_(n" expression="" applyOnUpdate="0"/>
    <default field="Nodo_tipo" expression="" applyOnUpdate="0"/>
    <default field="CF_nodo" expression="" applyOnUpdate="0"/>
    <default field="h_nodo_NT" expression="" applyOnUpdate="0"/>
    <default field="h_nodo_tp" expression="" applyOnUpdate="0"/>
    <default field="CItrd_nodo" expression="" applyOnUpdate="0"/>
    <default field="Tap_nodo" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint constraints="3" field="fid" notnull_strength="1" exp_strength="0" unique_strength="1"/>
    <constraint constraints="0" field="Y_I" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX_PAV_2" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX_PAV_1" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="X_I" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX03" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX02" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX01" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX_PROF_I" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="ID_COL" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX_POS" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="LABEL_VIS" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="ID_TRM_(N)" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="L" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="AUX_PROF_F" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="X_F" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Y_F" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="LABEL_X" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="LABEL_Y" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="h_col_p2" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="h_col_p1" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="h_tap_p2" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="h_tap_p1" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="S" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="DN" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Mat_col" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Caida_p2" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Caida_p2_h" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="n" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Qt_i" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Qt_f" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Q_i" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Q_f" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="yn_i" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="yn_f" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="yrel_i" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="yrel_f" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Trativa_i" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Trativa_f" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="V_i" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="V_f" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Vc" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Id_NODO_(n" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Nodo_tipo" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="CF_nodo" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="h_nodo_NT" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="h_nodo_tp" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="CItrd_nodo" notnull_strength="0" exp_strength="0" unique_strength="0"/>
    <constraint constraints="0" field="Tap_nodo" notnull_strength="0" exp_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" exp="" desc=""/>
    <constraint field="Y_I" exp="" desc=""/>
    <constraint field="AUX_PAV_2" exp="" desc=""/>
    <constraint field="AUX_PAV_1" exp="" desc=""/>
    <constraint field="X_I" exp="" desc=""/>
    <constraint field="AUX03" exp="" desc=""/>
    <constraint field="AUX02" exp="" desc=""/>
    <constraint field="AUX01" exp="" desc=""/>
    <constraint field="AUX_PROF_I" exp="" desc=""/>
    <constraint field="ID_COL" exp="" desc=""/>
    <constraint field="AUX_POS" exp="" desc=""/>
    <constraint field="LABEL_VIS" exp="" desc=""/>
    <constraint field="ID_TRM_(N)" exp="" desc=""/>
    <constraint field="L" exp="" desc=""/>
    <constraint field="AUX_PROF_F" exp="" desc=""/>
    <constraint field="X_F" exp="" desc=""/>
    <constraint field="Y_F" exp="" desc=""/>
    <constraint field="LABEL_X" exp="" desc=""/>
    <constraint field="LABEL_Y" exp="" desc=""/>
    <constraint field="h_col_p2" exp="" desc=""/>
    <constraint field="h_col_p1" exp="" desc=""/>
    <constraint field="h_tap_p2" exp="" desc=""/>
    <constraint field="h_tap_p1" exp="" desc=""/>
    <constraint field="S" exp="" desc=""/>
    <constraint field="DN" exp="" desc=""/>
    <constraint field="Mat_col" exp="" desc=""/>
    <constraint field="Caida_p2" exp="" desc=""/>
    <constraint field="Caida_p2_h" exp="" desc=""/>
    <constraint field="n" exp="" desc=""/>
    <constraint field="Qt_i" exp="" desc=""/>
    <constraint field="Qt_f" exp="" desc=""/>
    <constraint field="Q_i" exp="" desc=""/>
    <constraint field="Q_f" exp="" desc=""/>
    <constraint field="yn_i" exp="" desc=""/>
    <constraint field="yn_f" exp="" desc=""/>
    <constraint field="yrel_i" exp="" desc=""/>
    <constraint field="yrel_f" exp="" desc=""/>
    <constraint field="Trativa_i" exp="" desc=""/>
    <constraint field="Trativa_f" exp="" desc=""/>
    <constraint field="V_i" exp="" desc=""/>
    <constraint field="V_f" exp="" desc=""/>
    <constraint field="Vc" exp="" desc=""/>
    <constraint field="Id_NODO_(n" exp="" desc=""/>
    <constraint field="Nodo_tipo" exp="" desc=""/>
    <constraint field="CF_nodo" exp="" desc=""/>
    <constraint field="h_nodo_NT" exp="" desc=""/>
    <constraint field="h_nodo_tp" exp="" desc=""/>
    <constraint field="CItrd_nodo" exp="" desc=""/>
    <constraint field="Tap_nodo" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
    <actionsetting action="echo &quot;[% &quot;MY_FIELD&quot; %]&quot;" capture="1" notificationMessage="" icon="" name="Eco do valor de atributo" id="{b5858f8d-f8fb-4b98-be79-86a5523d917d}" isEnabledOnlyWhenEditable="0" shortTitle="" type="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting action="ogr2ogr -f &quot;ESRI Shapefile&quot; &quot;[% &quot;OUTPUT_PATH&quot; %]&quot; &quot;[% &quot;INPUT_FILE&quot; %]&quot;" capture="1" notificationMessage="" icon="" name="Rodar aplicação" id="{85d282c4-42b4-4289-b9e8-ddd5ef369847}" isEnabledOnlyWhenEditable="0" shortTitle="" type="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting action="QtGui.QMessageBox.information(None, &quot;Feature id&quot;, &quot;feature id is [% $id %]&quot;)" capture="0" notificationMessage="" icon="" name="Obter feição id" id="{2aefdaea-0c1a-45fa-a91f-e125711f5718}" isEnabledOnlyWhenEditable="0" shortTitle="" type="1">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting action="QtGui.QMessageBox.information(None, &quot;Current field's value&quot;, &quot;[% $currentfield %]&quot;)" capture="0" notificationMessage="" icon="" name="Selecionar valores de campo (Identificar ferramentas de identificação)" id="{c6d454ef-8e49-437c-b4b0-a7eac7293069}" isEnabledOnlyWhenEditable="0" shortTitle="" type="1">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting action="QtGui.QMessageBox.information(None, &quot;Clicked coords&quot;, &quot;layer: [% $layerid %]\ncoords: ([% $clickx %],[% $clicky %])&quot;)" capture="0" notificationMessage="" icon="" name="Coordenadas clicadas (Rodar ferramentas de ações de feições)" id="{45e71f22-f0ae-48c8-a49c-081fca9a14b6}" isEnabledOnlyWhenEditable="0" shortTitle="" type="1">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting action="[% &quot;PATH&quot; %]" capture="0" notificationMessage="" icon="" name="Abrir arquivo" id="{2c5c51aa-a85e-468a-a89a-b0a24ab45748}" isEnabledOnlyWhenEditable="0" shortTitle="" type="5">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting action="http://www.google.com/search?q=[% &quot;ATTRIBUTE&quot; %]" capture="0" notificationMessage="" icon="" name="Buscar na web valores de atributo" id="{ec39dd0e-459f-460e-8f4f-53add8f53fc6}" isEnabledOnlyWhenEditable="0" shortTitle="" type="5">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="">
    <columns>
      <column name="Y_I" width="-1" type="field" hidden="0"/>
      <column name="AUX_PAV_2" width="-1" type="field" hidden="0"/>
      <column name="AUX_PAV_1" width="-1" type="field" hidden="0"/>
      <column name="X_I" width="-1" type="field" hidden="0"/>
      <column name="AUX03" width="-1" type="field" hidden="0"/>
      <column name="AUX02" width="-1" type="field" hidden="0"/>
      <column name="AUX01" width="-1" type="field" hidden="0"/>
      <column name="AUX_PROF_I" width="-1" type="field" hidden="0"/>
      <column name="ID_COL" width="-1" type="field" hidden="0"/>
      <column name="AUX_POS" width="-1" type="field" hidden="0"/>
      <column name="LABEL_VIS" width="-1" type="field" hidden="0"/>
      <column name="ID_TRM_(N)" width="-1" type="field" hidden="0"/>
      <column name="L" width="-1" type="field" hidden="0"/>
      <column name="AUX_PROF_F" width="-1" type="field" hidden="0"/>
      <column name="X_F" width="-1" type="field" hidden="0"/>
      <column name="Y_F" width="-1" type="field" hidden="0"/>
      <column name="LABEL_X" width="-1" type="field" hidden="0"/>
      <column name="LABEL_Y" width="-1" type="field" hidden="0"/>
      <column name="h_col_p2" width="-1" type="field" hidden="0"/>
      <column name="h_col_p1" width="-1" type="field" hidden="0"/>
      <column name="S" width="-1" type="field" hidden="0"/>
      <column name="DN" width="-1" type="field" hidden="0"/>
      <column name="Mat_col" width="-1" type="field" hidden="0"/>
      <column name="Caida_p2" width="-1" type="field" hidden="0"/>
      <column name="Caida_p2_h" width="-1" type="field" hidden="0"/>
      <column name="n" width="-1" type="field" hidden="0"/>
      <column name="Qt_i" width="-1" type="field" hidden="0"/>
      <column name="Qt_f" width="-1" type="field" hidden="0"/>
      <column name="Q_i" width="-1" type="field" hidden="0"/>
      <column name="Q_f" width="-1" type="field" hidden="0"/>
      <column name="yn_i" width="-1" type="field" hidden="0"/>
      <column name="yn_f" width="-1" type="field" hidden="0"/>
      <column name="yrel_i" width="-1" type="field" hidden="0"/>
      <column name="yrel_f" width="-1" type="field" hidden="0"/>
      <column name="Trativa_i" width="-1" type="field" hidden="0"/>
      <column name="Trativa_f" width="-1" type="field" hidden="0"/>
      <column name="V_i" width="-1" type="field" hidden="0"/>
      <column name="V_f" width="-1" type="field" hidden="0"/>
      <column name="Vc" width="-1" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
      <column name="h_tap_p2" width="-1" type="field" hidden="0"/>
      <column name="h_tap_p1" width="-1" type="field" hidden="0"/>
      <column name="fid" width="-1" type="field" hidden="0"/>
      <column name="Id_NODO_(n" width="-1" type="field" hidden="0"/>
      <column name="Nodo_tipo" width="-1" type="field" hidden="0"/>
      <column name="CF_nodo" width="-1" type="field" hidden="0"/>
      <column name="h_nodo_NT" width="-1" type="field" hidden="0"/>
      <column name="h_nodo_tp" width="-1" type="field" hidden="0"/>
      <column name="CItrd_nodo" width="-1" type="field" hidden="0"/>
      <column name="Tap_nodo" width="-1" type="field" hidden="0"/>
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
    <field name="CF_nodo" editable="1"/>
    <field name="CItrd_nodo" editable="1"/>
    <field name="Caida_p2" editable="1"/>
    <field name="Caida_p2_h" editable="1"/>
    <field name="DN" editable="1"/>
    <field name="ID_COL" editable="1"/>
    <field name="ID_TRM_(N)" editable="1"/>
    <field name="Id_NODO_(n" editable="1"/>
    <field name="L" editable="1"/>
    <field name="LABEL_VIS" editable="1"/>
    <field name="LABEL_X" editable="1"/>
    <field name="LABEL_Y" editable="1"/>
    <field name="Mat_col" editable="1"/>
    <field name="Nodo_tipo" editable="1"/>
    <field name="Q_f" editable="1"/>
    <field name="Q_i" editable="1"/>
    <field name="Qt_f" editable="1"/>
    <field name="Qt_i" editable="1"/>
    <field name="S" editable="1"/>
    <field name="Tap_nodo" editable="1"/>
    <field name="Trativa_f" editable="1"/>
    <field name="Trativa_i" editable="1"/>
    <field name="V_f" editable="1"/>
    <field name="V_i" editable="1"/>
    <field name="Vc" editable="1"/>
    <field name="X_F" editable="1"/>
    <field name="X_I" editable="1"/>
    <field name="Y_F" editable="1"/>
    <field name="Y_I" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="h_col_p1" editable="1"/>
    <field name="h_col_p2" editable="1"/>
    <field name="h_nodo_NT" editable="1"/>
    <field name="h_nodo_tp" editable="1"/>
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
    <field name="CF_nodo" labelOnTop="0"/>
    <field name="CItrd_nodo" labelOnTop="0"/>
    <field name="Caida_p2" labelOnTop="0"/>
    <field name="Caida_p2_h" labelOnTop="0"/>
    <field name="DN" labelOnTop="0"/>
    <field name="ID_COL" labelOnTop="0"/>
    <field name="ID_TRM_(N)" labelOnTop="0"/>
    <field name="Id_NODO_(n" labelOnTop="0"/>
    <field name="L" labelOnTop="0"/>
    <field name="LABEL_VIS" labelOnTop="0"/>
    <field name="LABEL_X" labelOnTop="0"/>
    <field name="LABEL_Y" labelOnTop="0"/>
    <field name="Mat_col" labelOnTop="0"/>
    <field name="Nodo_tipo" labelOnTop="0"/>
    <field name="Q_f" labelOnTop="0"/>
    <field name="Q_i" labelOnTop="0"/>
    <field name="Qt_f" labelOnTop="0"/>
    <field name="Qt_i" labelOnTop="0"/>
    <field name="S" labelOnTop="0"/>
    <field name="Tap_nodo" labelOnTop="0"/>
    <field name="Trativa_f" labelOnTop="0"/>
    <field name="Trativa_i" labelOnTop="0"/>
    <field name="V_f" labelOnTop="0"/>
    <field name="V_i" labelOnTop="0"/>
    <field name="Vc" labelOnTop="0"/>
    <field name="X_F" labelOnTop="0"/>
    <field name="X_I" labelOnTop="0"/>
    <field name="Y_F" labelOnTop="0"/>
    <field name="Y_I" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="h_col_p1" labelOnTop="0"/>
    <field name="h_col_p2" labelOnTop="0"/>
    <field name="h_nodo_NT" labelOnTop="0"/>
    <field name="h_nodo_tp" labelOnTop="0"/>
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
