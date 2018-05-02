from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from boards.models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

    """Step2
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
    """

    # return HttpResponse('Hello, World!')  # Step1


def board_topics(request, pk):

    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404

    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})