# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Speaker Recognition", pos = wx.DefaultPosition, size = wx.Size( 390,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 390,300 ), wx.Size( 390,300 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hardware" ), wx.VERTICAL )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		sbSizer2.Add( self.m_choice1, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_toggleBtn1 = wx.ToggleButton( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Listen", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_gauge1 = wx.Gauge( sbSizer2.GetStaticBox(), wx.ID_ANY, 1000, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge1.SetValue( 0 )
		bSizer5.Add( self.m_gauge1, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Result" ), wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap1 = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,40 ), 0 )
		self.m_bitmap1.SetMaxSize( wx.Size( 40,40 ) )

		bSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		self.m_gauge2 = wx.Gauge( sbSizer4.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge2.SetValue( 0 )
		bSizer2.Add( self.m_gauge2, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap2 = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,40 ), 0 )
		self.m_bitmap2.SetMaxSize( wx.Size( 40,40 ) )

		bSizer3.Add( self.m_bitmap2, 0, wx.ALL, 5 )

		self.m_gauge3 = wx.Gauge( sbSizer4.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge3.SetValue( 0 )
		bSizer3.Add( self.m_gauge3, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap3 = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,40 ), 0 )
		self.m_bitmap3.SetMaxSize( wx.Size( 40,40 ) )

		bSizer4.Add( self.m_bitmap3, 0, wx.ALL, 5 )

		self.m_gauge4 = wx.Gauge( sbSizer4.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_gauge4.SetValue( 0 )
		bSizer4.Add( self.m_gauge4, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer4.Add( bSizer4, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, self.m_timer1.GetId() )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Closing )
		self.m_toggleBtn1.Bind( wx.EVT_TOGGLEBUTTON, self.startStop )
		self.Bind( wx.EVT_TIMER, self.tick, id=self.m_timer1.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Closing( self, event ):
		event.Skip()

	def startStop( self, event ):
		event.Skip()

	def tick( self, event ):
		event.Skip()


