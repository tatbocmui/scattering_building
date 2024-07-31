import tkinter as tk
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import data_manager as dm
def create_display_frame(parent):
    display_frame = ttk.Frame(parent, padding="10 10 10 10", borderwidth=2, relief='solid')
    # display_frame.grid(row=2, column=1, sticky="nw")
    return display_frame

def draw_object(input_vars, check_vars, radio_vars, drawing_vars, directory_vars, num_windows_var, window_vars_list, mother_display_frame):
    data= dm.data_create(input_vars, check_vars, radio_vars, drawing_vars, directory_vars, num_windows_var, window_vars_list)

    tplate=data['tplate']

    # Extract the tholes and tglass, tConDuctingSlab data and store in arrays
    tholes = data['tholes']
    tglass = data['tglass']
    fig = plt.figure(figsize=(4.5, 4), dpi=100)
    ax = fig.add_subplot(projection='3d', proj_type = 'ortho')
    ax.set_xlim([-tplate["aLx"]/2,tplate["aLx"]/2])
    ax.set_ylim([-tplate["aLy"]/2,tplate["aLy"]/2])
    ax.set_zlim([-tplate["aLz"],0])
    ax.set_aspect('equal', adjustable='box')
    # Draw Building
    rect = Rectangle((-tplate["aLx"]/2, -tplate["aLy"]/2), tplate["aLx"], tplate["aLy"], linewidth=1, edgecolor='black', facecolor='dimgrey', alpha=0.2)
    ax.add_patch(rect)
    art3d.pathpatch_2d_to_3d(rect, z=0, zdir="z")
    
    rect = Rectangle((-tplate["aLx"]/2, -tplate["aLy"]/2), tplate["aLx"], tplate["aLy"], linewidth=1, edgecolor='black', facecolor='dimgrey', alpha=0.2)
    ax.add_patch(rect)
    art3d.pathpatch_2d_to_3d(rect, z=-tplate["aLz"], zdir="z")
    
    rect = Rectangle((-tplate["aLy"]/2, 0), tplate["aLy"], -tplate["aLz"], linewidth=1, edgecolor='black', facecolor='dimgrey', alpha=0.2)
    ax.add_patch(rect)
    art3d.pathpatch_2d_to_3d(rect, z=tplate["aLx"]/2, zdir="x")
    
    rect = Rectangle((-tplate["aLy"]/2, 0), tplate["aLy"], -tplate["aLz"], linewidth=1, edgecolor='black', facecolor='dimgrey', alpha=0.2)
    ax.add_patch(rect)
    art3d.pathpatch_2d_to_3d(rect, z=-tplate["aLx"]/2, zdir="x")
    
    rect = Rectangle((-tplate["aLx"]/2, 0), tplate["aLx"], -tplate["aLz"], linewidth=1, edgecolor='black', facecolor='dimgrey', alpha=0.2)
    ax.add_patch(rect)
    art3d.pathpatch_2d_to_3d(rect, z=tplate["aLy"]/2, zdir="y")
    
    rect = Rectangle((-tplate["aLx"]/2, 0), tplate["aLx"], -tplate["aLz"], linewidth=1, edgecolor='black', facecolor='dimgrey', alpha=0.2)
    ax.add_patch(rect)
    art3d.pathpatch_2d_to_3d(rect, z=-tplate["aLy"]/2, zdir="y")
    
    # Draw window
    for i in range(data["iNumberWindows"]):
        if(tholes[i]['positionHole']=='x'):
            awy=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='k', facecolor='w', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adx, zdir=tholes[i]['positionHole'])
        if(tholes[i]['positionHole']=='y'):
            awx=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='k', facecolor='w', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=ady, zdir=tholes[i]['positionHole'])
        if(tholes[i]['positionHole']=='-x'):
            awy=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='k', facecolor='w', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adx, zdir=tholes[i]['positionHole'].replace("-",""))
        if(tholes[i]['positionHole']=='-y'):
            awx=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='k', facecolor='w', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=ady, zdir=tholes[i]['positionHole'].replace("-",""))
    # Draw glass
    for i in range(data["iNumberWindows"]):
        if(tglass[i]['aGlassThickness']!=0):
            if(tholes[i]['positionHole']=='x'):
                awy=tholes[i]['aa']
                awz=tholes[i]['ab']
                adx=tholes[i]['adx']
                ady=tholes[i]['ady']
                adz=tholes[i]['adz']
                ac1=tglass[i]['ac1']
                ac2=tglass[i]['ac1']+tglass[i]['aGlassThickness']
                rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac1, zdir=tholes[i]['positionHole'])
                #Draw thickness of glass
                rect = Rectangle((-ac1, ady+awy/2), -tglass[i]['aGlassThickness'], -awy, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
                
                rect = Rectangle((-ac1, ady+awy/2), -tglass[i]['aGlassThickness'], -awy, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
            
                rect = Rectangle((-ac1, adz+awz/2), -tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=ady+awy/2, zdir="y")
                
                rect = Rectangle((-ac1, adz+awz/2), -tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=ady-awy/2, zdir="y")

                rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac2, zdir=tholes[i]['positionHole'])
            if(tholes[i]['positionHole']=='y'):
                awx=tholes[i]['aa']
                awz=tholes[i]['ab']
                adx=tholes[i]['adx']
                ady=tholes[i]['ady']
                adz=tholes[i]['adz']
                ac1=tglass[i]['ac1']
                ac2=tglass[i]['ac1']+tglass[i]['aGlassThickness']
                rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac1, zdir=tholes[i]['positionHole'])
                #Draw thickness of glass
                rect = Rectangle((adx-awx/2,-ac1), awx, -tglass[i]['aGlassThickness'], linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
                
                rect = Rectangle((adx-awx/2,-ac1), awx, -tglass[i]['aGlassThickness'], linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
            
                rect = Rectangle((-ac1, adz+awz/2), -tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adx+awx/2, zdir="x")
                
                rect = Rectangle((-ac1, adz+awz/2), -tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adx-awx/2, zdir="x")

                rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac2, zdir=tholes[i]['positionHole'])
            if(tholes[i]['positionHole']=='-x'):
                awy=tholes[i]['aa']
                awz=tholes[i]['ab']
                adx=tholes[i]['adx']
                ady=tholes[i]['ady']
                adz=tholes[i]['adz']
                ac1=tglass[i]['ac1']
                ac2=tglass[i]['ac1']-tglass[i]['aGlassThickness']
                rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac1, zdir=tholes[i]['positionHole'].replace("-",""))
                #Draw thickness of glass
                rect = Rectangle((-ac1, ady+awy/2), tglass[i]['aGlassThickness'], -awy, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
                
                rect = Rectangle((-ac1, ady+awy/2), tglass[i]['aGlassThickness'], -awy, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
            
                rect = Rectangle((-ac1, adz+awz/2), tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=ady+awy/2, zdir="y")
                
                rect = Rectangle((-ac1, adz+awz/2), tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=ady-awy/2, zdir="y")

                rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac2, zdir=tholes[i]['positionHole'].replace("-",""))
            if(tholes[i]['positionHole']=='-y'):
                awx=tholes[i]['aa']
                awz=tholes[i]['ab']
                adx=tholes[i]['adx']
                ady=tholes[i]['ady']
                adz=tholes[i]['adz']
                ac1=tglass[i]['ac1']
                ac2=tglass[i]['ac1']-tglass[i]['aGlassThickness']
                rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac1, zdir=tholes[i]['positionHole'].replace("-",""))
                #Draw thickness of glass
                rect = Rectangle((adx-awx/2,-ac1), awx, tglass[i]['aGlassThickness'], linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
                
                rect = Rectangle((adx-awx/2,-ac1), awx, tglass[i]['aGlassThickness'], linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
            
                rect = Rectangle((-ac1, adz+awz/2), tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adx+awx/2, zdir="x")
                
                rect = Rectangle((-ac1, adz+awz/2), tglass[i]['aGlassThickness'], -awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=adx-awx/2, zdir="x")

                rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='b', facecolor='b', alpha=0.5)
                ax.add_patch(rect)
                art3d.pathpatch_2d_to_3d(rect, z=-ac2, zdir=tholes[i]['positionHole'].replace("-",""))   
    # Draw conducting Room
    for i in range(data["iNumberWindows"]):
        if(tholes[i]['positionHole']=='x'):
            awy=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            acs=tholes[i]['ac']
            rect = Rectangle((-acs, ady+awy/2), tplate["aLx"]/2+acs, -awy, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
            
            rect = Rectangle((-acs, ady+awy/2), tplate["aLx"]/2+acs, -awy, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
        
            rect = Rectangle((-acs, adz+awz/2), tplate["aLx"]/2+acs, -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=ady+awy/2, zdir="y")
            
            rect = Rectangle((-acs, adz+awz/2), tplate["aLx"]/2+acs, -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=ady-awy/2, zdir="y")

            rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=-acs, zdir=tholes[i]['positionHole'])
        if(tholes[i]['positionHole']=='y'):
            awx=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            acs=tholes[i]['ac']

            rect = Rectangle((adx-awx/2,-acs), awx, tplate["aLy"]/2+acs, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
            
            rect = Rectangle((adx-awx/2,-acs), awx, tplate["aLy"]/2+acs, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
        
            rect = Rectangle((-acs, adz+awz/2), tplate["aLy"]/2+acs, -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adx+awx/2, zdir="x")
            
            rect = Rectangle((-acs, adz+awz/2), tplate["aLy"]/2+acs, -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adx-awx/2, zdir="x")

            rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=-acs, zdir=tholes[i]['positionHole'])
        if(tholes[i]['positionHole']=='-x'):
            awy=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            acs=tholes[i]['ac']
            rect = Rectangle((-acs, ady+awy/2), -(tplate["aLx"]/2-acs), -awy, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
            
            rect = Rectangle((-acs, ady+awy/2), -(tplate["aLx"]/2-acs), -awy, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
        
            rect = Rectangle((-acs, adz+awz/2), -(tplate["aLx"]/2-acs), -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=ady+awy/2, zdir="y")
            
            rect = Rectangle((-acs, adz+awz/2), -(tplate["aLx"]/2-acs), -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=ady-awy/2, zdir="y")

            rect = Rectangle((ady-awy/2, adz-awz/2), awy, awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=-acs, zdir=tholes[i]['positionHole'].replace("-",""))
        if(tholes[i]['positionHole']=='-y'):
            awx=tholes[i]['aa']
            awz=tholes[i]['ab']
            adx=tholes[i]['adx']
            ady=tholes[i]['ady']
            adz=tholes[i]['adz']
            acs=tholes[i]['ac']

            rect = Rectangle((adx-awx/2,-acs), awx, -(tplate["aLy"]/2-acs), linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz+awz/2, zdir="z")
            
            rect = Rectangle((adx-awx/2,-acs), awx, -(tplate["aLy"]/2-acs), linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adz-awz/2, zdir="z")
        
            rect = Rectangle((-acs, adz+awz/2), -(tplate["aLy"]/2-acs), -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adx+awx/2, zdir="x")
            
            rect = Rectangle((-acs, adz+awz/2), -(tplate["aLy"]/2-acs), -awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=adx-awx/2, zdir="x")

            rect = Rectangle((adx-awx/2, adz-awz/2), awx, awz, linewidth=1, edgecolor='b', facecolor='c', alpha=0.5)
            ax.add_patch(rect)
            art3d.pathpatch_2d_to_3d(rect, z=-acs, zdir=tholes[i]['positionHole'].replace("-",""))         



    # #Draw arrow axis
    # xaxis = Arrow(0, 0, tplate["aLx"]/2+5, 0, width=10, facecolor='r', alpha=1)
    # ax.add_patch(xaxis)
    # art3d.pathpatch_2d_to_3d(xaxis, z=0, zdir="z")    
    # ax.text(tplate["aLx"]/2+10, 0, 0, "X", ha="center", va="center", color="r", fontsize=20)
    # yaxis = Arrow(0, 0, 0, tplate["aLy"]/2+5, width=10, facecolor='b', alpha=1)
    # ax.add_patch(yaxis)
    # art3d.pathpatch_2d_to_3d(yaxis, z=0, zdir="z")
    # ax.text(0, tplate["aLy"]/2+10, 0, "Y", ha="center", va="center", color="b", fontsize=20)
    # zaxis = Arrow(0, 0, 0, tplate["aLz"]/2-2, width=10, facecolor='g', alpha=1)
    # ax.add_patch(zaxis)
    # art3d.pathpatch_2d_to_3d(zaxis, z=0, zdir="y")
    # ax.text(0, 0, tplate["aLz"]/2, "Z", ha="center", va="center", color="g", fontsize=20)
    # # Set the axis labels
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')
    ax.set_axis_off()
    # Rotate the axes and update
    # Enable mouse-based rotation
    rotate = True
    def on_click(event):
        global rotate
        if rotate:
            ax.view_init(elev=event.ydata, azim=event.xdata)
            fig.canvas.draw_idle()

    # # Gán sự kiện cho chuột cuộn lên và xuống
    # def on_scroll(event):
    #     if event.button == 'up':
    #         scale_factor = 0.9  # Zoom in
    #     elif event.button == 'down':
    #         scale_factor = 1.1  # Zoom out
    #     else:
    #         return

    #     # Get the current scaling factors
    #     xlim = ax.get_xlim()
    #     ylim = ax.get_ylim()
    #     zlim = ax.get_zlim()

    #     # Calculate the zoomed limits
    #     new_xlim = (xlim[0] * scale_factor, xlim[1] * scale_factor)
    #     new_ylim = (ylim[0] * scale_factor, ylim[1] * scale_factor)
    #     new_zlim = (zlim[0] * scale_factor, zlim[1] * scale_factor)

    #     # Set the updated limits
    #     ax.set_xlim(new_xlim)
    #     ax.set_ylim(new_ylim)
    #     ax.set_zlim(new_zlim)
    #     # Redraw the plot
    #     fig.canvas.draw()

    # # Connect the scroll event to the mouse wheel zooming function
    # fig.canvas.mpl_connect("scroll_event", on_scroll)
    # # Cập nhật lại cửa sổ figure
    # fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    # # fig.canvas.draw()
    # # fig.show()

    # # Embed the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=mother_display_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    zoom_button_frame = ttk.Frame(mother_display_frame, padding="10 10 10 10")
    zoom_button_frame.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))
    # Add Zoom In button
    zoom_in_button = ttk.Button(zoom_button_frame, text="Zoom In", command=lambda: zoom('in', ax, fig))
    zoom_in_button.grid(row=0, column=0, sticky="w")  # Corrected grid placement

    # Add Zoom Out button
    zoom_out_button = ttk.Button(zoom_button_frame, text="Zoom Out", command=lambda: zoom('out', ax, fig))
    zoom_out_button.grid(row=0, column=1, sticky="w")  # Corrected grid placement
    
def zoom(direction, ax, fig):
    scale_factor = 0.9 if direction == 'in' else 1.1

    # Get the current scaling factors
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    zlim = ax.get_zlim()

    # Calculate the zoomed limits
    new_xlim = (xlim[0] * scale_factor, xlim[1] * scale_factor)
    new_ylim = (ylim[0] * scale_factor, ylim[1] * scale_factor)
    new_zlim = (zlim[0] * scale_factor, zlim[1] * scale_factor)

    # Set the updated limits
    ax.set_xlim(new_xlim)
    ax.set_ylim(new_ylim)
    ax.set_zlim(new_zlim)

    # Redraw the plot
    fig.canvas.draw()
