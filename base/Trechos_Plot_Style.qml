<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.4.2-Madeira" maxScale="100000" simplifyAlgorithm="0" simplifyLocal="1" readOnly="0" simplifyMaxScale="1" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" labelsEnabled="1" simplifyDrawingHints="1" simplifyDrawingTol="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" type="RuleRenderer" enableorderby="0" forceraster="0">
    <rules key="{7b6772ff-b392-462e-910b-bc97815c9341}">
      <rule key="{89fa5778-836a-4f4c-8b63-e9f38d289fe2}" symbol="0" filter=" &quot;L&quot; &lt;> 0"/>
      <rule key="{97cbed74-e7cf-4194-8afd-bb33570d294a}" symbol="1" filter=" &quot;Caida_p2&quot; ='D'"/>
      <rule key="{a324e7fc-3afb-48c8-86ba-ac3b5a893d55}" symbol="2" filter=" &quot;Caida_p2_h&quot;   > 0 and   &quot;Caida_p2&quot;   = 'TC'"/>
    </rules>
    <symbols>
      <symbol type="line" name="0" alpha="1" clip_to_extent="1">
        <layer class="SimpleLine" enabled="1" pass="0" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="draw_inside_polygon" v="0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="line_color" v="4,0,241,255"/>
          <prop k="line_style" v="solid"/>
          <prop k="line_width" v="1"/>
          <prop k="line_width_unit" v="MapUnit"/>
          <prop k="offset" v="0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="MarkerLine" enabled="1" pass="1" locked="0">
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="vertex"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@1" alpha="1" clip_to_extent="1">
            <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="170,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.6"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MapUnit"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="6"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MapUnit"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer class="MarkerLine" enabled="1" pass="2" locked="0">
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="centralpoint"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@0@2" alpha="1" clip_to_extent="1">
            <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="4,0,241,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="arrowhead"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MapUnit"/>
              <prop k="outline_color" v="67,67,67,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="1.3"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MapUnit"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="7"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MapUnit"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="name">
                      <Option type="bool" name="active" value="false"/>
                      <Option type="QString" name="field" value="COTAF"/>
                      <Option type="int" name="type" value="2"/>
                    </Option>
                  </Option>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="line" name="1" alpha="1" clip_to_extent="1">
        <layer class="MarkerLine" enabled="1" pass="0" locked="0">
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="lastvertex"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@1@0" alpha="1" clip_to_extent="1">
            <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="4,0,241,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="-6,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MapUnit"/>
              <prop k="outline_color" v="0,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.5"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MapUnit"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="3"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MapUnit"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol type="line" name="2" alpha="1" clip_to_extent="1">
        <layer class="MarkerLine" enabled="1" pass="0" locked="0">
          <prop k="interval" v="3"/>
          <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="interval_unit" v="MM"/>
          <prop k="offset" v="0"/>
          <prop k="offset_along_line" v="0"/>
          <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_along_line_unit" v="MM"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="placement" v="lastvertex"/>
          <prop k="rotate" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol type="marker" name="@2@0" alpha="1" clip_to_extent="1">
            <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,0,0,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="-6,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MapUnit"/>
              <prop k="outline_color" v="0,0,0,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.5"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MapUnit"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="3"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MapUnit"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" name="name" value=""/>
                  <Option name="properties"/>
                  <Option type="QString" name="type" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{210e84d3-6f74-4ee6-a572-d6280966362c}">
      <rule key="{382426db-a4d8-4c26-9f13-9afe8f25aba4}" filter=" &quot;Caida_p2_h&quot; &lt;= 0.0399 or  &quot;Caida_p2_h&quot;  is NULL">
        <settings>
          <text-style fontCapitals="0" fontItalic="0" namedStyle="Normal" multilineHeight="1" fontSize="8.25" fontSizeUnit="Point" textOpacity="1" textColor="0,0,0,255" fieldName="   &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xa;     ''  || '\n' ||&#xa;     'Ø' ||   &quot;DN&quot;    || '\n' || &#xa;        &quot;S&quot;  " fontLetterSpacing="0" previewBkgrdColor="#ffffff" blendMode="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" fontFamily="MS Shell Dlg 2" fontStrikeout="0" fontWordSpacing="0" useSubstitutions="0" isExpression="1">
            <text-buffer bufferDraw="1" bufferSize="1" bufferOpacity="0.4" bufferBlendMode="0" bufferSizeUnits="MapUnit" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferNoFill="0" bufferJoinStyle="64"/>
            <background shapeSizeUnit="MM" shapeBlendMode="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeDraw="0" shapeBorderWidth="0" shapeSizeY="0" shapeJoinStyle="64" shapeSizeX="0" shapeRadiiUnit="MM" shapeSizeType="0" shapeRadiiX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeSVGFile="" shapeOpacity="1" shapeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowRadiusUnit="MM" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowUnder="0" shadowOffsetDist="1" shadowOpacity="0.7" shadowColor="0,0,0,255" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowOffsetAngle="135"/>
            <substitutions/>
          </text-style>
          <text-format multilineAlign="1" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" formatNumbers="0" plussign="0" addDirectionSymbol="0" decimals="3" wrapChar="" autoWrapLength="0"/>
          <placement dist="0" placement="2" maxCurvedCharAngleIn="20" xOffset="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" quadOffset="4" repeatDistance="0" distUnits="MM" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-20" priority="5" distMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" offsetType="0" preserveRotation="1" centroidInside="0" offsetUnits="MapUnit" yOffset="0" fitInPolygonOnly="0" centroidWhole="0"/>
          <rendering obstacleFactor="1" scaleVisibility="1" fontMaxPixelSize="10000" displayAll="0" obstacle="1" fontLimitPixelSize="0" maxNumLabels="2000" mergeLines="0" scaleMin="1" minFeatureSize="0" upsidedownLabels="0" obstacleType="0" labelPerPart="0" limitNumLabels="0" scaleMax="4000" drawLabels="1" fontMinPixelSize="3" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option type="Map" name="properties">
                <Option type="Map" name="PositionX">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="field" value="LABEL_X"/>
                  <Option type="int" name="type" value="2"/>
                </Option>
                <Option type="Map" name="PositionY">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="field" value="LABEL_Y"/>
                  <Option type="int" name="type" value="2"/>
                </Option>
                <Option type="Map" name="Show">
                  <Option type="bool" name="active" value="true"/>
                  <Option type="QString" name="field" value="LABEL_VIS"/>
                  <Option type="int" name="type" value="2"/>
                </Option>
              </Option>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{b2c7e36c-79a6-4db7-9b5d-db41de7dd944}" filter=" &quot;Caida_p2_h&quot;  &lt;> 0 and  &quot;Caida_p2&quot;  ='TC'">
        <settings>
          <text-style fontCapitals="0" fontItalic="0" namedStyle="Normal" multilineHeight="1" fontSize="8.25" fontSizeUnit="Point" textOpacity="1" textColor="0,0,0,255" fieldName="    &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xd;&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xd;&#xa;     ''  || '\n' ||&#xd;&#xa;&#x9;  ''  || '\n' ||&#xd;&#xa;      'Ø' ||   &quot;DN&quot;    || '\n' || &#xd;&#xa;        &quot;S&quot;  || '\n' || &#xd;&#xa;&#x9;&#x9; &quot;Caida_p2&quot;   || ' '||   &quot;Caida_p2_h&quot;" fontLetterSpacing="0" previewBkgrdColor="#ffffff" blendMode="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" fontFamily="MS Shell Dlg 2" fontStrikeout="0" fontWordSpacing="0" useSubstitutions="0" isExpression="1">
            <text-buffer bufferDraw="1" bufferSize="1" bufferOpacity="0.4" bufferBlendMode="0" bufferSizeUnits="MapUnit" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferNoFill="0" bufferJoinStyle="64"/>
            <background shapeSizeUnit="MM" shapeBlendMode="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeDraw="0" shapeBorderWidth="0" shapeSizeY="0" shapeJoinStyle="64" shapeSizeX="0" shapeRadiiUnit="MM" shapeSizeType="0" shapeRadiiX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeSVGFile="" shapeOpacity="1" shapeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowRadiusUnit="MM" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowUnder="0" shadowOffsetDist="1" shadowOpacity="0.7" shadowColor="0,0,0,255" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowOffsetAngle="135"/>
            <substitutions/>
          </text-style>
          <text-format multilineAlign="1" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" formatNumbers="0" plussign="0" addDirectionSymbol="0" decimals="3" wrapChar="" autoWrapLength="0"/>
          <placement dist="0" placement="2" maxCurvedCharAngleIn="20" xOffset="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" quadOffset="4" repeatDistance="0" distUnits="MM" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-20" priority="5" distMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" offsetType="0" preserveRotation="1" centroidInside="0" offsetUnits="MapUnit" yOffset="0" fitInPolygonOnly="0" centroidWhole="0"/>
          <rendering obstacleFactor="1" scaleVisibility="1" fontMaxPixelSize="10000" displayAll="0" obstacle="1" fontLimitPixelSize="0" maxNumLabels="2000" mergeLines="0" scaleMin="1" minFeatureSize="0" upsidedownLabels="0" obstacleType="0" labelPerPart="0" limitNumLabels="0" scaleMax="4000" drawLabels="1" fontMinPixelSize="3" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </dd_properties>
        </settings>
      </rule>
      <rule key="{12efec36-1411-4efa-927d-329fa19ad7b6}" filter=" &quot;Caida_p2_h&quot; > 0.0399 and &quot;Caida_p2&quot; ='D'">
        <settings>
          <text-style fontCapitals="0" fontItalic="0" namedStyle="Normal" multilineHeight="1" fontSize="8.25" fontSizeUnit="Point" textOpacity="1" textColor="0,0,0,255" fieldName="    &quot;ID_TRM_(N)&quot;  ||  '\n'  ||&#xd;&#xa;     &quot;L&quot;    || 'm'  ||  '\n'  ||&#xd;&#xa;     ''  || '\n' ||&#xd;&#xa;&#x9;  ''  || '\n' ||&#xd;&#xa;      'Ø' ||   &quot;DN&quot;    || '\n' || &#xd;&#xa;        &quot;S&quot;  || '\n' || &#xd;&#xa;&#x9;&#x9;  'D'   || ' '||  &quot;Caida_p2_h&quot;" fontLetterSpacing="0" previewBkgrdColor="#ffffff" blendMode="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" fontFamily="MS Shell Dlg 2" fontStrikeout="0" fontWordSpacing="0" useSubstitutions="0" isExpression="1">
            <text-buffer bufferDraw="1" bufferSize="1" bufferOpacity="0.4" bufferBlendMode="0" bufferSizeUnits="MapUnit" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferNoFill="0" bufferJoinStyle="64"/>
            <background shapeSizeUnit="MM" shapeBlendMode="0" shapeRotation="0" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeDraw="0" shapeBorderWidth="0" shapeSizeY="0" shapeJoinStyle="64" shapeSizeX="0" shapeRadiiUnit="MM" shapeSizeType="0" shapeRadiiX="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeOffsetY="0" shapeSVGFile="" shapeOpacity="1" shapeType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRotationType="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetUnit="MM" shapeFillColor="255,255,255,255" shapeRadiiY="0"/>
            <shadow shadowRadiusUnit="MM" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowBlendMode="6" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowUnder="0" shadowOffsetDist="1" shadowOpacity="0.7" shadowColor="0,0,0,255" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowDraw="0" shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowOffsetAngle="135"/>
            <substitutions/>
          </text-style>
          <text-format multilineAlign="1" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" rightDirectionSymbol=">" formatNumbers="0" plussign="0" addDirectionSymbol="0" decimals="3" wrapChar="" autoWrapLength="0"/>
          <placement dist="0" placement="2" maxCurvedCharAngleIn="20" xOffset="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" quadOffset="4" repeatDistance="0" distUnits="MM" repeatDistanceUnits="MM" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-20" priority="5" distMapUnitScale="3x:0,0,0,0,0,0" rotationAngle="0" offsetType="0" preserveRotation="1" centroidInside="0" offsetUnits="MapUnit" yOffset="0" fitInPolygonOnly="0" centroidWhole="0"/>
          <rendering obstacleFactor="1" scaleVisibility="1" fontMaxPixelSize="10000" displayAll="0" obstacle="1" fontLimitPixelSize="0" maxNumLabels="2000" mergeLines="0" scaleMin="1" minFeatureSize="0" upsidedownLabels="0" obstacleType="0" labelPerPart="0" limitNumLabels="0" scaleMax="4000" drawLabels="1" fontMinPixelSize="3" zIndex="0"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
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
    <DiagramCategory height="15" minScaleDenominator="100000" penWidth="0" backgroundAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" barWidth="5" backgroundColor="#ffffff" opacity="1" sizeScale="3x:0,0,0,0,0,0" lineSizeType="MM" enabled="0" minimumSize="0" penAlpha="255" scaleDependency="Area" diagramOrientation="Up" width="15" maxScaleDenominator="1e+08" rotationOffset="270" labelPlacementMethod="XHeight" scaleBasedVisibility="0" sizeType="MM" penColor="#000000">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" placement="2" obstacle="0" showAll="1" zIndex="0" priority="0" linePlacementFlags="2">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option type="Map" name="properties">
          <Option type="Map" name="show">
            <Option type="bool" name="active" value="true"/>
            <Option type="QString" name="field" value="Y_I"/>
            <Option type="int" name="type" value="2"/>
          </Option>
        </Option>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="Y_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PAV_2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PAV_1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="X_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX03">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX02">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX01">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PROF_I">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_COL">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_POS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_VIS">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="ID_TRM_(N)">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="L">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="AUX_PROF_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="X_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Y_F">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_X">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="LABEL_Y">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_col_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_col_p1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_tap_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="h_tap_p1">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="S">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="DN">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Mat_col">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Caida_p2">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Caida_p2_h">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="n">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Qt_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Qt_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Q_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Q_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yn_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yn_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yrel_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="yrel_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Trativa_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Trativa_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="V_i">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="V_f">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
    <field name="Vc">
      <editWidget type="TextEdit">
        <config>
          <Option type="Map">
            <Option type="QString" name="IsMultiline" value="0"/>
            <Option type="QString" name="UseHtml" value="0"/>
          </Option>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="Y_I" name="" index="0"/>
    <alias field="AUX_PAV_2" name="" index="1"/>
    <alias field="AUX_PAV_1" name="" index="2"/>
    <alias field="X_I" name="" index="3"/>
    <alias field="AUX03" name="" index="4"/>
    <alias field="AUX02" name="" index="5"/>
    <alias field="AUX01" name="" index="6"/>
    <alias field="AUX_PROF_I" name="" index="7"/>
    <alias field="ID_COL" name="" index="8"/>
    <alias field="AUX_POS" name="" index="9"/>
    <alias field="LABEL_VIS" name="" index="10"/>
    <alias field="ID_TRM_(N)" name="" index="11"/>
    <alias field="L" name="" index="12"/>
    <alias field="AUX_PROF_F" name="" index="13"/>
    <alias field="X_F" name="" index="14"/>
    <alias field="Y_F" name="" index="15"/>
    <alias field="LABEL_X" name="" index="16"/>
    <alias field="LABEL_Y" name="" index="17"/>
    <alias field="h_col_p2" name="" index="18"/>
    <alias field="h_col_p1" name="" index="19"/>
    <alias field="h_tap_p2" name="" index="20"/>
    <alias field="h_tap_p1" name="" index="21"/>
    <alias field="S" name="" index="22"/>
    <alias field="DN" name="" index="23"/>
    <alias field="Mat_col" name="" index="24"/>
    <alias field="Caida_p2" name="" index="25"/>
    <alias field="Caida_p2_h" name="" index="26"/>
    <alias field="n" name="" index="27"/>
    <alias field="Qt_i" name="" index="28"/>
    <alias field="Qt_f" name="" index="29"/>
    <alias field="Q_i" name="" index="30"/>
    <alias field="Q_f" name="" index="31"/>
    <alias field="yn_i" name="" index="32"/>
    <alias field="yn_f" name="" index="33"/>
    <alias field="yrel_i" name="" index="34"/>
    <alias field="yrel_f" name="" index="35"/>
    <alias field="Trativa_i" name="" index="36"/>
    <alias field="Trativa_f" name="" index="37"/>
    <alias field="V_i" name="" index="38"/>
    <alias field="V_f" name="" index="39"/>
    <alias field="Vc" name="" index="40"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="Y_I" applyOnUpdate="0" expression=""/>
    <default field="AUX_PAV_2" applyOnUpdate="0" expression=""/>
    <default field="AUX_PAV_1" applyOnUpdate="0" expression=""/>
    <default field="X_I" applyOnUpdate="0" expression=""/>
    <default field="AUX03" applyOnUpdate="0" expression=""/>
    <default field="AUX02" applyOnUpdate="0" expression=""/>
    <default field="AUX01" applyOnUpdate="0" expression=""/>
    <default field="AUX_PROF_I" applyOnUpdate="0" expression=""/>
    <default field="ID_COL" applyOnUpdate="0" expression=""/>
    <default field="AUX_POS" applyOnUpdate="0" expression=""/>
    <default field="LABEL_VIS" applyOnUpdate="0" expression=""/>
    <default field="ID_TRM_(N)" applyOnUpdate="0" expression=""/>
    <default field="L" applyOnUpdate="0" expression=""/>
    <default field="AUX_PROF_F" applyOnUpdate="0" expression=""/>
    <default field="X_F" applyOnUpdate="0" expression=""/>
    <default field="Y_F" applyOnUpdate="0" expression=""/>
    <default field="LABEL_X" applyOnUpdate="0" expression=""/>
    <default field="LABEL_Y" applyOnUpdate="0" expression=""/>
    <default field="h_col_p2" applyOnUpdate="0" expression=""/>
    <default field="h_col_p1" applyOnUpdate="0" expression=""/>
    <default field="h_tap_p2" applyOnUpdate="0" expression=""/>
    <default field="h_tap_p1" applyOnUpdate="0" expression=""/>
    <default field="S" applyOnUpdate="0" expression=""/>
    <default field="DN" applyOnUpdate="0" expression=""/>
    <default field="Mat_col" applyOnUpdate="0" expression=""/>
    <default field="Caida_p2" applyOnUpdate="0" expression=""/>
    <default field="Caida_p2_h" applyOnUpdate="0" expression=""/>
    <default field="n" applyOnUpdate="0" expression=""/>
    <default field="Qt_i" applyOnUpdate="0" expression=""/>
    <default field="Qt_f" applyOnUpdate="0" expression=""/>
    <default field="Q_i" applyOnUpdate="0" expression=""/>
    <default field="Q_f" applyOnUpdate="0" expression=""/>
    <default field="yn_i" applyOnUpdate="0" expression=""/>
    <default field="yn_f" applyOnUpdate="0" expression=""/>
    <default field="yrel_i" applyOnUpdate="0" expression=""/>
    <default field="yrel_f" applyOnUpdate="0" expression=""/>
    <default field="Trativa_i" applyOnUpdate="0" expression=""/>
    <default field="Trativa_f" applyOnUpdate="0" expression=""/>
    <default field="V_i" applyOnUpdate="0" expression=""/>
    <default field="V_f" applyOnUpdate="0" expression=""/>
    <default field="Vc" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="Y_I" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX_PAV_2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX_PAV_1" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="X_I" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX03" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX02" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX01" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX_PROF_I" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="ID_COL" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX_POS" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="LABEL_VIS" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="ID_TRM_(N)" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="L" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="AUX_PROF_F" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="X_F" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Y_F" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="LABEL_X" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="LABEL_Y" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="h_col_p2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="h_col_p1" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="h_tap_p2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="h_tap_p1" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="S" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="DN" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Mat_col" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Caida_p2" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Caida_p2_h" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="n" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Qt_i" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Qt_f" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Q_i" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Q_f" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="yn_i" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="yn_f" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="yrel_i" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="yrel_f" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Trativa_i" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Trativa_f" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="V_i" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="V_f" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
    <constraint field="Vc" constraints="0" exp_strength="0" notnull_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="Y_I" desc="" exp=""/>
    <constraint field="AUX_PAV_2" desc="" exp=""/>
    <constraint field="AUX_PAV_1" desc="" exp=""/>
    <constraint field="X_I" desc="" exp=""/>
    <constraint field="AUX03" desc="" exp=""/>
    <constraint field="AUX02" desc="" exp=""/>
    <constraint field="AUX01" desc="" exp=""/>
    <constraint field="AUX_PROF_I" desc="" exp=""/>
    <constraint field="ID_COL" desc="" exp=""/>
    <constraint field="AUX_POS" desc="" exp=""/>
    <constraint field="LABEL_VIS" desc="" exp=""/>
    <constraint field="ID_TRM_(N)" desc="" exp=""/>
    <constraint field="L" desc="" exp=""/>
    <constraint field="AUX_PROF_F" desc="" exp=""/>
    <constraint field="X_F" desc="" exp=""/>
    <constraint field="Y_F" desc="" exp=""/>
    <constraint field="LABEL_X" desc="" exp=""/>
    <constraint field="LABEL_Y" desc="" exp=""/>
    <constraint field="h_col_p2" desc="" exp=""/>
    <constraint field="h_col_p1" desc="" exp=""/>
    <constraint field="h_tap_p2" desc="" exp=""/>
    <constraint field="h_tap_p1" desc="" exp=""/>
    <constraint field="S" desc="" exp=""/>
    <constraint field="DN" desc="" exp=""/>
    <constraint field="Mat_col" desc="" exp=""/>
    <constraint field="Caida_p2" desc="" exp=""/>
    <constraint field="Caida_p2_h" desc="" exp=""/>
    <constraint field="n" desc="" exp=""/>
    <constraint field="Qt_i" desc="" exp=""/>
    <constraint field="Qt_f" desc="" exp=""/>
    <constraint field="Q_i" desc="" exp=""/>
    <constraint field="Q_f" desc="" exp=""/>
    <constraint field="yn_i" desc="" exp=""/>
    <constraint field="yn_f" desc="" exp=""/>
    <constraint field="yrel_i" desc="" exp=""/>
    <constraint field="yrel_f" desc="" exp=""/>
    <constraint field="Trativa_i" desc="" exp=""/>
    <constraint field="Trativa_f" desc="" exp=""/>
    <constraint field="V_i" desc="" exp=""/>
    <constraint field="V_f" desc="" exp=""/>
    <constraint field="Vc" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
    <actionsetting id="{ad4a5a2a-ef0c-4c1d-9cd8-6cdc2ba6307e}" icon="" shortTitle="" capture="1" type="0" name="Eco do valor de atributo" action="echo &quot;[% &quot;MY_FIELD&quot; %]&quot;" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting id="{f8dd24b3-f9dd-4254-9bd2-edfa88884d23}" icon="" shortTitle="" capture="1" type="0" name="Rodar aplicação" action="ogr2ogr -f &quot;ESRI Shapefile&quot; &quot;[% &quot;OUTPUT_PATH&quot; %]&quot; &quot;[% &quot;INPUT_FILE&quot; %]&quot;" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting id="{573742bb-2074-4b7a-98ff-2fcb0d396ac0}" icon="" shortTitle="" capture="0" type="1" name="Obter feição id" action="QtGui.QMessageBox.information(None, &quot;Feature id&quot;, &quot;feature id is [% $id %]&quot;)" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting id="{4d95b140-35b1-47d7-ac24-d07aeccb9943}" icon="" shortTitle="" capture="0" type="1" name="Selecionar valores de campo (Identificar ferramentas de identificação)" action="QtGui.QMessageBox.information(None, &quot;Current field's value&quot;, &quot;[% $currentfield %]&quot;)" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting id="{b99a2137-afab-4e63-9476-0126582c05f3}" icon="" shortTitle="" capture="0" type="1" name="Coordenadas clicadas (Rodar ferramentas de ações de feições)" action="QtGui.QMessageBox.information(None, &quot;Clicked coords&quot;, &quot;layer: [% $layerid %]\ncoords: ([% $clickx %],[% $clicky %])&quot;)" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting id="{000b9da1-45eb-4328-b893-f21cd5dfbcc1}" icon="" shortTitle="" capture="0" type="5" name="Abrir arquivo" action="[% &quot;PATH&quot; %]" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
    <actionsetting id="{4d3fb12a-e485-479a-a265-2079485d73d6}" icon="" shortTitle="" capture="0" type="5" name="Buscar na web valores de atributo" action="http://www.google.com/search?q=[% &quot;ATTRIBUTE&quot; %]" notificationMessage="" isEnabledOnlyWhenEditable="0">
      <actionScope id="Field"/>
      <actionScope id="Feature"/>
      <actionScope id="Canvas"/>
    </actionsetting>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column type="field" name="Y_I" width="-1" hidden="0"/>
      <column type="field" name="AUX_PAV_2" width="-1" hidden="0"/>
      <column type="field" name="AUX_PAV_1" width="-1" hidden="0"/>
      <column type="field" name="X_I" width="-1" hidden="0"/>
      <column type="field" name="AUX03" width="-1" hidden="0"/>
      <column type="field" name="AUX02" width="-1" hidden="0"/>
      <column type="field" name="AUX01" width="-1" hidden="0"/>
      <column type="field" name="AUX_PROF_I" width="-1" hidden="0"/>
      <column type="field" name="ID_COL" width="-1" hidden="0"/>
      <column type="field" name="AUX_POS" width="-1" hidden="0"/>
      <column type="field" name="LABEL_VIS" width="-1" hidden="0"/>
      <column type="field" name="ID_TRM_(N)" width="-1" hidden="0"/>
      <column type="field" name="L" width="-1" hidden="0"/>
      <column type="field" name="AUX_PROF_F" width="-1" hidden="0"/>
      <column type="field" name="X_F" width="-1" hidden="0"/>
      <column type="field" name="Y_F" width="-1" hidden="0"/>
      <column type="field" name="LABEL_X" width="-1" hidden="0"/>
      <column type="field" name="LABEL_Y" width="-1" hidden="0"/>
      <column type="field" name="h_col_p2" width="-1" hidden="0"/>
      <column type="field" name="h_col_p1" width="-1" hidden="0"/>
      <column type="field" name="S" width="-1" hidden="0"/>
      <column type="field" name="DN" width="-1" hidden="0"/>
      <column type="field" name="Mat_col" width="-1" hidden="0"/>
      <column type="field" name="Caida_p2" width="-1" hidden="0"/>
      <column type="field" name="Caida_p2_h" width="-1" hidden="0"/>
      <column type="field" name="n" width="-1" hidden="0"/>
      <column type="field" name="Qt_i" width="-1" hidden="0"/>
      <column type="field" name="Qt_f" width="-1" hidden="0"/>
      <column type="field" name="Q_i" width="-1" hidden="0"/>
      <column type="field" name="Q_f" width="-1" hidden="0"/>
      <column type="field" name="yn_i" width="-1" hidden="0"/>
      <column type="field" name="yn_f" width="-1" hidden="0"/>
      <column type="field" name="yrel_i" width="-1" hidden="0"/>
      <column type="field" name="yrel_f" width="-1" hidden="0"/>
      <column type="field" name="Trativa_i" width="-1" hidden="0"/>
      <column type="field" name="Trativa_f" width="-1" hidden="0"/>
      <column type="field" name="V_i" width="-1" hidden="0"/>
      <column type="field" name="V_f" width="-1" hidden="0"/>
      <column type="field" name="Vc" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
      <column type="field" name="h_tap_p2" width="-1" hidden="0"/>
      <column type="field" name="h_tap_p1" width="-1" hidden="0"/>
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
    <field labelOnTop="0" name="AUX01"/>
    <field labelOnTop="0" name="AUX02"/>
    <field labelOnTop="0" name="AUX03"/>
    <field labelOnTop="0" name="AUX_PAV_1"/>
    <field labelOnTop="0" name="AUX_PAV_2"/>
    <field labelOnTop="0" name="AUX_POS"/>
    <field labelOnTop="0" name="AUX_PROF_F"/>
    <field labelOnTop="0" name="AUX_PROF_I"/>
    <field labelOnTop="0" name="Caida_p2"/>
    <field labelOnTop="0" name="Caida_p2_h"/>
    <field labelOnTop="0" name="DN"/>
    <field labelOnTop="0" name="ID_COL"/>
    <field labelOnTop="0" name="ID_TRM_(N)"/>
    <field labelOnTop="0" name="L"/>
    <field labelOnTop="0" name="LABEL_VIS"/>
    <field labelOnTop="0" name="LABEL_X"/>
    <field labelOnTop="0" name="LABEL_Y"/>
    <field labelOnTop="0" name="Mat_col"/>
    <field labelOnTop="0" name="Q_f"/>
    <field labelOnTop="0" name="Q_i"/>
    <field labelOnTop="0" name="Qt_f"/>
    <field labelOnTop="0" name="Qt_i"/>
    <field labelOnTop="0" name="S"/>
    <field labelOnTop="0" name="Trativa_f"/>
    <field labelOnTop="0" name="Trativa_i"/>
    <field labelOnTop="0" name="V_f"/>
    <field labelOnTop="0" name="V_i"/>
    <field labelOnTop="0" name="Vc"/>
    <field labelOnTop="0" name="X_F"/>
    <field labelOnTop="0" name="X_I"/>
    <field labelOnTop="0" name="Y_F"/>
    <field labelOnTop="0" name="Y_I"/>
    <field labelOnTop="0" name="h_col_p1"/>
    <field labelOnTop="0" name="h_col_p2"/>
    <field labelOnTop="0" name="h_tap_p1"/>
    <field labelOnTop="0" name="h_tap_p2"/>
    <field labelOnTop="0" name="n"/>
    <field labelOnTop="0" name="yn_f"/>
    <field labelOnTop="0" name="yn_i"/>
    <field labelOnTop="0" name="yrel_f"/>
    <field labelOnTop="0" name="yrel_i"/>
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
