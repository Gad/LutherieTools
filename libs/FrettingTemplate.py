"""This file is part of LuTOOL. LuTOOL is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any later 
version.

LuTOOL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with LuTOOL. 
If not, see <https://www.gnu.org/licenses/>. 
    
    Ce fichier fait partie de LuTOOL. LuTOOL est un logiciel libre; vous pouvez le 
redistribuer ou le modifier suivant les termes de la GNU General Public License telle 
que publiée par la Free Software Foundation; soit la version 3 de la licence, soit 
(à votre gré) toute version ultérieure.
LuTOOL est distribué dans l'espoir qu'il sera utile, mais SANS AUCUNE GARANTIE; 
sans même la garantie tacite de QUALITÉ MARCHANDE ou d'ADÉQUATION à UN BUT PARTICULIER. 
Consultez la GNU General Public License pour plus de détails.
Vous devez avoir reçu une copie de la GNU General Public License en même temps que 
LuTOOL; si ce n'est pas le cas, consultez <http://www.gnu.org/licenses>.
"""

import cairo

from io import BytesIO
from math import pi
import logging


class FrettingTemplate:
    def __init__(self, r1_length : float, r1_length_unit : str, r1_frets_number : int, 
                 r1_marks_enabled: bool, r2_length : float, r2_length_unit : str, 
                 r2_frets_number : int, r2_marks_enabled: bool):
        
        LENGTHS, UNITS, FRETS, MARKS, self.HEIGHT = [r1_length, r2_length], \
            [r1_length_unit, r2_length_unit], [r1_frets_number, r2_frets_number],\
            [r1_marks_enabled, r2_marks_enabled], 60
        
        # my zero is the nut and the nut is 13mm away from the left closure 
        # so we'll need to translate everything by 13mm right to fit the viewport and 
        # avoid issues with the renderer
        logging.debug('create new fretting template')
        CONST_TRANSLATE = 13  

        for i,unit in enumerate(UNITS): 
            if unit!='mm': 
                LENGTHS[i]=self.convert_to_mm(LENGTHS[i])

        output=BytesIO()
        output.flush()
        surface = cairo.SVGSurface(output,max(LENGTHS)+100, self.HEIGHT)
        surface.set_document_unit(cairo.SVG_UNIT_MM)
        self.ctx = cairo.Context(surface)
        self.ctx.scale(1,1)
        self.ctx.set_line_width(0.5)
        self.ctx.translate(CONST_TRANSLATE,0)
        print(LENGTHS)
        
        max_point=[]
        for k in range(2):
            CONST_DIV = 17.817
            
            new_length=LENGTHS[k]
            fret_points=[0]
            for i in range(1,FRETS[k]+1):
                fret_points.append(round(new_length/CONST_DIV+fret_points[i-1],3))
                new_length-=new_length/CONST_DIV

            
            drawing_points=[]
            for point in fret_points:
                drawing_points.append([point-1,point+1])

            # drawing the two scale length
            
            # add left side with the start at the nut 
            #print(drawing_points)
            
            self.ctx.set_source_rgb(1,0,0)
            self.ctx.move_to(0,0)
        
            #---------- Nut ------------
            self.ctx.move_to(drawing_points[0][1], k*self.HEIGHT)
            self.ctx.line_to(drawing_points[0][1], k*self.HEIGHT+(-1)**k*3) 
            self.ctx.line_to(drawing_points[0][1]-1, k*self.HEIGHT+(-1)**k*4.50)
            self.ctx.line_to(drawing_points[0][0], k*self.HEIGHT+(-1)**k*3)
            self.ctx.line_to(drawing_points[0][0], k*self.HEIGHT) 
            #----------------------------

            #---------- pre-Nut ------------
            self.ctx.line_to(drawing_points[0][1]-7, k*self.HEIGHT)
            self.ctx.line_to(drawing_points[0][1]-7, k*self.HEIGHT+(-1)**k*3) 
            self.ctx.line_to(drawing_points[0][1]-8, k*self.HEIGHT+(-1)**k*4.5)
            self.ctx.line_to(drawing_points[0][0]-7, k*self.HEIGHT+(-1)**k*3)
            self.ctx.line_to(drawing_points[0][0]-7, k*self.HEIGHT)
            #-------------------------------

            #----------- left closure-------
            self.ctx.line_to(drawing_points[0][0]-12, k*self.HEIGHT)
            self.ctx.line_to(drawing_points[0][0]-12, self.HEIGHT) 
            #--------------------------------
            self.ctx.stroke()
            #------------ draw scalelength and marks
            for i in range(len(drawing_points)-1):

                self.ctx.set_source_rgb(0,1,0)
                if r1_marks_enabled and k==0 : 
                    if i in [2,4,6,8,14,16,18,20]:
                        self.draw_mark(fret_points[i], fret_points[i+1], 0)
                    elif i in [11,23]:
                        self.draw_double_marks(fret_points[i], fret_points[i+1], 0)
                if r2_marks_enabled and k==1: 
                    if i in [2,4,6,8,14,16,18,20]:
                        self.draw_mark(fret_points[i], fret_points[i+1], 1)
                    elif i in [11,23]:
                        self.draw_double_marks(fret_points[i], fret_points[i+1], 1)

                self.ctx.stroke()
                self.ctx.set_source_rgb(1,0,0)

                self.ctx.move_to(drawing_points[i][1], k*self.HEIGHT)
                self.ctx.line_to(drawing_points[i+1][0], k*self.HEIGHT)
                
                self.ctx.line_to(drawing_points[i+1][0], k*self.HEIGHT+(-1)**k*3)
                self.ctx.line_to(drawing_points[i+1][0]+1, k*self.HEIGHT+(-1)**k*4.5) 
                self.ctx.line_to(drawing_points[i+1][1], k*self.HEIGHT+(-1)**k*3) 
                self.ctx.line_to(drawing_points[i+1][1], k*self.HEIGHT)
                self.ctx.stroke()

            

            # store the last fret_point of each scale +1 , this is where the scale ends
            max_point.append(drawing_points[-1][1])
            print(max(max_point)) 
            #self.ctx.stroke()  
        #self.ctx.set_source_rgb(0,0,1)
        #----------- right closure-------

        self.total_length=max(max_point)+29
        self.ctx.new_sub_path()
        self.ctx.move_to(max_point[0], 0)
        self.ctx.line_to(self.total_length, 0)
        self.ctx.line_to(self.total_length, self.HEIGHT)
        self.ctx.line_to(max_point[1], self.HEIGHT)


        #draw 8mm hole
        self.ctx.new_sub_path()
        self.ctx.arc(max(max_point)+29-10, self.HEIGHT/2, 4,0,2*pi) 

        self.ctx.stroke()    
        
        

        #Text test

        self.ctx.select_font_face("1CamBam_Stick_2",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
        self.ctx.set_font_size(9)
        self.ctx.set_source_rgb(0,1,0)

        t_width=[0,0] #list of text width
        #first row
        if r1_length_unit=="mm":
            text=str(int(r1_length))+"mm"
        else: 
            text=str(r1_length)+'"' 
        
        
       
        _, _, t_width[0], _, _, _ = self.ctx.text_extents(text)
        self.ctx.move_to(self.total_length-3, 5)
        
        self.ctx.rotate(pi)
        self.ctx.text_path(text)
        self.ctx.rotate(pi)
        #second row
        if r2_length_unit=="mm":
            text=str(int(r2_length))+"mm"
        else: 
            text=str(r2_length)+'"' 
        
        
       
        _, _, t_width[1], _, _, _ = self.ctx.text_extents(text)
        self.ctx.move_to(self.total_length-3, self.HEIGHT-10)
        
        self.ctx.rotate(pi)
        self.ctx.text_path(text)

        self.ctx.set_line_width(0.2)
        self.ctx.stroke()
        self.ctx.rotate(pi) #back on earth
        # draw mark line if requested
        
        self.ctx.set_source_rgb(0,1,0)
        if MARKS[0]:
            self.ctx.move_to(min(max_point[0],self.total_length-t_width[0]-4),7.5)
            self.ctx.line_to(-8,7.5)

        if MARKS[1]:
            self.ctx.move_to(min(max_point[1],self.total_length-t_width[1]-4),self.HEIGHT-7.5)
            self.ctx.line_to(-8,self.HEIGHT-7.5) 
        self.ctx.stroke()

        # draw zero mark
        # first two vertical segments
        self.ctx.move_to(0,5)
        self.ctx.line_to(0,self.HEIGHT//2-10)
        self.ctx.move_to(0,self.HEIGHT//2+10)
        self.ctx.line_to(0,self.HEIGHT-5)

        #then draw "0"
        self.ctx.set_font_size(10)
        _, _, t_width_0, t_height, _, _ = self.ctx.text_extents("0")
        self.ctx.move_to(0-t_width_0/2,self.HEIGHT//2+t_height/2)
        

        self.ctx.text_path("0")
        self.ctx.stroke()

        self.ctx.save()
        self.ctx.scale(0.5,0.5)
        self.ctx.restore()


        
        surface.finish() #that's enough !
        
        self.SVGoutput=output.getvalue()

    def convert_to_mm(self, inchs_distance):
        return round(inchs_distance * 25.4,2)
    
    def draw_mark(self, starting_frette, ending_frette, row):
        middle=(starting_frette+ending_frette)/2
        self.ctx.new_sub_path()
        
        # drill hole
        self.ctx.set_source_rgb(1,0,0)
        self.ctx.arc(middle, row*self.HEIGHT+(-1)**row*7.5, 0.75, 0,2*pi)
        self.ctx.stroke()
        #draw circle
        self.ctx.set_source_rgb(0,1,0)
        self.ctx.arc(middle, row*self.HEIGHT+(-1)**row*7.5, 1.75, 0,2*pi)
        #draw parallel lines
        self.ctx.move_to(middle-3.75, row*self.HEIGHT+(-1)**row*5)
        self.ctx.line_to(middle+3.75, row*self.HEIGHT+(-1)**row*5)
        self.ctx.move_to(middle-3.75, row*self.HEIGHT+(-1)**row*10)
        self.ctx.line_to(middle+3.75, row*self.HEIGHT+(-1)**row*10)
        #draw cross
        self.ctx.move_to(middle, row*self.HEIGHT+(-1)**row*(7.5+2))
        self.ctx.line_to(middle, row*self.HEIGHT+(-1)**row*(7.5-2))

        

    def draw_double_marks(self, starting_frette, ending_frette, row):
        middle=(starting_frette+ending_frette)/2 #middle between 2 frettes, will come handy  # noqa: E501
        self.ctx.new_sub_path()
        # drill holes
        self.ctx.set_source_rgb(1,0,0)
        self.ctx.arc(middle-2.5, row*self.HEIGHT+(-1)**row*7.5, 0.75, 0,2*pi)
        self.ctx.new_sub_path()
        self.ctx.arc(middle+2.5, row*self.HEIGHT+(-1)**row*7.5, 0.75, 0,2*pi)
        self.ctx.stroke()
        #draw circles
        self.ctx.set_source_rgb(0,1,0)
        self.ctx.arc(middle-2.5, row*self.HEIGHT+(-1)**row*7.5, 1.75, 0,2*pi)
        self.ctx.new_sub_path()
        self.ctx.arc(middle+2.5, row*self.HEIGHT+(-1)**row*7.5, 1.75, 0,2*pi)
        #draw parallel lines
        self.ctx.move_to(middle-6.25, row*self.HEIGHT+(-1)**row*5)
        self.ctx.line_to(middle+6.25, row*self.HEIGHT+(-1)**row*5)
        self.ctx.move_to(middle-6.25, row*self.HEIGHT+(-1)**row*10)
        self.ctx.line_to(middle+6.25, row*self.HEIGHT+(-1)**row*10)
        #draw crosses
        self.ctx.move_to(middle-2.5, row*self.HEIGHT+(-1)**row*(7.5+2))
        self.ctx.line_to(middle-2.5, row*self.HEIGHT+(-1)**row*(7.5-2)) 
        self.ctx.move_to(middle+2.5, row*self.HEIGHT+(-1)**row*(7.5+2))
        self.ctx.line_to(middle+2.5, row*self.HEIGHT+(-1)**row*(7.5-2)) 