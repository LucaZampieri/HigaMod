function createfigure(X1, Y1, X2, Y2)
%CREATEFIGURE(X1,Y1,X2,Y2)
%  X1:  vector of x data
%  Y1:  vector of y data
%  X2:  vector of x data
%  Y2:  vector of y data

%  Auto-generated by MATLAB on 05-Oct-2013 13:09:28

% Create figure
figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1,'FontSize',20);
box(axes1,'on');
grid(axes1,'on');
hold(axes1,'all');

% Create plot
plot(X1,Y1,'Parent',axes1,'LineWidth',3,'DisplayName','\fontsize{15} f(x)',...
    'Color',[0 0 0]);

% Create plot
plot(X2,Y2,'Parent',axes1,'LineWidth',3,'LineStyle','--','Color',[1 0 0],...
    'DisplayName','\fontsize{15}Projection m=16');
ylim([-0.1,1.6])
% Create legend
legend1 = legend(axes1,'show');
set(legend1,'YColor',[1 1 1],'XColor',[1 1 1],...
    'location','best');
export_fig(figure1, 'filename','steepprog','-eps','-transparent')
